import tkinter as tk
import serial
import tkinter.messagebox
import threading
import time
import keyboard
import queue
import sqlite3
import pyautogui

##############아두이노 파이썬 연결##############
try:
    ARDUINO = serial.Serial("com3", 9600, timeout=1,
                                xonxoff=False, rtscts=False, dsrdtr=False)
    ARDUINO.close()
except:
    pass

########################함수####################

def ConnectDB():
    con = sqlite3.connect('Keyarray.db')
    cursor = con.cursor()
    return cursor

def Fetch_DBTable(num):
    global KeySetting
    global ButtonBasket
    ButtonBasket = []
    KeySetting = []
    cur = ConnectDB()
    sql = "select * from keytable{}".format(num)
    cur.execute(sql)
    db_keysetting = cur.fetchall()
    for i in range(KeyAmount):
        KeySetting.append(db_keysetting[0][i])
    cur.close()

def thread_sample():
    global GAMEPAD_LOOP
    while GAMEPAD_LOOP == True:
        try:
            communicate_arduino = ARDUINO.readline()
            input_key = communicate_arduino[1:15]
            SetPressAndReleaseRPG(input_key)
            UpdateKeyIndex(input_key)
        except:
            GAMEPAD_LOOP = False
            tkinter.messagebox.showwarning("경고", "선이 빠저버렸습니다.")
        
def UpdateKeyIndex(input_key):
    for i in range(KeyAmount):
        if input_key[i:i+1] == b'1':
            keyIndex[i] = 1
        elif input_key[i:i+1] == b'0':
            keyIndex[i] = 0
    
def SetPressAndReleaseRPG(input_key):
    for i in range(KeyAmount):
        if input_key[i:i+1] == b'1' and keyIndex[i] == 0:
            keyboard.press(KeySetting[i])
        if input_key[i:i+1] == b'0' and keyIndex[i] == 1:
            keyboard.release(KeySetting[i])

    
def SetPressAndReleaseFPS(input_key):
    pass
    '''
    #0=위 1=아래 2=왼쪽 3= 오른쪽
    dx=0
    dy=0
    #↑
    if input_key[0:1] == b'1':
        dy = dy+10
    #↓ 
    if input_key[1:2] == b'1':
        dy = dy-10
    #←
    if input_key[2:3] == b'1':
        dx = dx+10
    #→
    if input_key[3:4] == b'1':
        dx = dx-10
    MouseMove(dx,dy)   
    for i in range(4,KeyAmount-4):
        if input_key[i:i+1] == b'1' and keyIndex[i] == 0:
            keyboard.press(KeySetting[i])
        if input_key[i:i+1] == b'0' and keyIndex[i] == 1:
            keyboard.release(KeySetting[i])
    '''

def MouseMove(dx, dy):
    CurrentX, CurrentY = pyautogui.position()
    pyautogui.moveTo(CurrentX+dx, CurrentY+dy, 0.03, pyautogui.easeOutQuad)

    
def SaveDB(num):
    cur = ConnectDB()
    for i in range(KeyAmount):
        sql = "update KeyTable{0} set Key{1} = '{2}'".format(num,i+1,ButtonBasket[i].text)
        KeySetting[i] = ButtonBasket[i].text
        cur.execute(sql)
    cur.execute("commit")
    cur.close()
        
def RunGamepadLoop(button):
    global GAMEPAD_LOOP
    if GAMEPAD_LOOP == False:
        GAMEPAD_LOOP = True
        ARDUINO.open()
        gamepad_loop_thread = threading.Thread(target = thread_sample)
        gamepad_loop_thread.start()
        button.configure(text = "stop")
    else:
        GAMEPAD_LOOP = False
        ARDUINO.close()
        button.configure(text = "run!")

########################tkinter##################################
class TkinerRoot(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.title("유연한 게임패드")
        self.geometry("500x400+400+200")
        self.resizable(False,False)
        self.SwitchFrame(Home)   
    def SwitchFrame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.place(x=0, y=0, width=500, height=400)

        

class KeyRecordingThread(threading.Thread):
    def __init__(self, q):
        threading.Thread.__init__(self)
        self.q = q

    def run(self):
        while True:
            if keyboard.read_key() != None:
                self.q.put(keyboard.read_key())
                break


    
class NewWindow(tk.Tk):
    def __init__(self, index):
        tk.Tk.__init__(self)
        self.ReadKey = False
        self.index = index
        self.Key = ""
        self.Rooping = 0
        self.frame = tk.Frame(self)
        self.frame.place(x=0, y=0, width=200, height=150)
        self.title("새로운 창")
        self.geometry("200x150+300+200")
        self.resizable(False,False)
        self.recordinglabel = tk.Label(self.frame, text = "Recording.")
        self.recordinglabel.place(x=60, y=20, width=100, height=20)
        self.OKbutton = tk.Button(self.frame, text = "OK", command = self.DefineKey)
        self.OKbutton.place(x=45, y=70, width=50, height=20)
        self.Cancelbutton = tk.Button(self.frame, text = "Cancel", command = self.ReDefine)
        self.Cancelbutton.place(x=105, y=70, width=50, height=20)
        self.after(300,self.ChangeTextRecording)
        self.q = queue.Queue(1)
        self.RunThread()

    def ChangeTextRecording(self):
        if self.ReadKey == False:
            self.Rooping = self.Rooping + 1
            if self.Rooping %3 == 0:
                self.recordinglabel.configure(text=  "Recording.")
            if self.Rooping %3 == 1:
                self.recordinglabel.configure(text=  "Recording..")
            if self.Rooping %3 == 2:
                self.recordinglabel.configure(text=  "Recording...")
            self.after(300,self.ChangeTextRecording)

    def RunThread(self):
        KeyRecordingThread(self.q).start()
        self.after(0, self.BindKeyboard)
        
    def BindKeyboard(self):
        try:
            self.Key = self.q.get(0)
            if self.Key != None:
                self.ReadKey = True
                self.recordinglabel.configure(text= self.Key)
                return
        except queue.Empty:
            self.after(100, self.BindKeyboard)

    def DefineKey(self):
        if self.Key == "":
            tkinter.messagebox.showwarning("주의", "키를 입력해주세요.")
        else:
            for i in range(KeyAmount):
                if ButtonBasket[i].text == self.Key:
                    if ButtonBasket[self.index].text == self.Key:
                        break
                    tkinter.messagebox.showwarning("주의", "동일한 키가 이미 있습니다.")
                    self.ReDefine()
                    return
            ButtonBasket[self.index].text = self.Key
            ButtonBasket[self.index].button.configure(text = self.Key)
            self.destroy()

        
    def ReDefine(self):
        self.ReadKey = False
        self.Key = ""
        self.after(0,self.ChangeTextRecording)
        self.RunThread()


class Keybutton(tk.Frame):
    def __init__(self,master,index,text,x,y):
        self.text = text
        self.index = index
        self.button = tk.Button(master ,text = text,command = lambda: self.change_setting(master))
        self.button.place(x=x, y=y,width=40,height=25)
        
    def change_setting(self, master):
        window = NewWindow(self.index)
        


class Home(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.RPGButton = tk.Button(self, text = "RPG" ,command = lambda: master.SwitchFrame(RPGPage1))
        self.RPGButton.place(x=255, y=340, width=40, height=25)
        self.FPSButton = tk.Button(self, text="FPS",  command=lambda: master.SwitchFrame(FPSPage1))
        self.FPSButton.place(x =205 , y =340,width = 40,height=25)

    
class RPGPage1(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        Fetch_DBTable(1)
        for i in range(14):
            key = Keybutton(self,i, KeySetting[i],Tk_button_locate[i][0],Tk_button_locate[i][1])
            ButtonBasket.append(key)
        self.SaveButton = tk.Button(self, text = "save" ,command = lambda: SaveDB(1))
        self.SaveButton.place(x=255, y=340, width=40, height=25)
        self.Runbutton = tk.Button(self, text="run!",  command=lambda: RunGamepadLoop(self.Runbutton))
        self.Runbutton.place(x =205 , y =340,width = 40,height=25)
        tk.Button(self, text="1번셋팅", state = tk.DISABLED).place(x=0, y=0, width=60, height=25)
        tk.Button(self, text="2번셋팅", command = lambda: master.SwitchFrame(RPGPage2)).place(x=60, y=0, width=60, height=25)
        tk.Button(self, text="3번셋팅", command = lambda: master.SwitchFrame(RPGPage3)).place(x=120, y=0, width=60, height=25)
        tk.Button(self, text="Back", command = lambda: master.SwitchFrame(Home)).place(x=440, y=0, width=60, height=25)



class RPGPage2(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        Fetch_DBTable(2)
        for i in range(14):
            key = Keybutton(self,i, KeySetting[i],Tk_button_locate[i][0],Tk_button_locate[i][1])
            ButtonBasket.append(key)
        self.SaveButton = tk.Button(self, text = "save" ,command = lambda: SaveDB(2))
        self.SaveButton.place(x=255, y=340, width=40, height=25)
        self.Runbutton = tk.Button(self, text="run!",  command=lambda: RunGamepadLoop(self.Runbutton))
        self.Runbutton.place(x =205 , y =340,width = 40,height=25)
        tk.Button(self, text="1번셋팅", command = lambda: master.SwitchFrame(RPGPage1)).place(x=0, y=0, width=60, height=25)
        tk.Button(self, text="2번셋팅", state = tk.DISABLED).place(x=60, y=0, width=60, height=25)
        tk.Button(self, text="3번셋팅", command = lambda: master.SwitchFrame(RPGPage3)).place(x=120, y=0, width=60, height=25)
        tk.Button(self, text="Back", command = lambda: master.SwitchFrame(Home)).place(x=440, y=0, width=60, height=25)

class RPGPage3(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        Fetch_DBTable(3)
        for i in range(14):
            key = Keybutton(self,i, KeySetting[i],Tk_button_locate[i][0],Tk_button_locate[i][1])
            ButtonBasket.append(key)
        self.SaveButton = tk.Button(self, text = "save" ,command = lambda: SaveDB(3))
        self.SaveButton.place(x=255, y=340, width=40, height=25)
        self.Runbutton = tk.Button(self, text="run!",  command=lambda: RunGamepadLoop(self.Runbutton))
        self.Runbutton.place(x =205 , y =340,width = 40,height=25)
        tk.Button(self, text="1번셋팅", command = lambda: master.SwitchFrame(RPGPage1)).place(x=0, y=0, width=60, height=25)
        tk.Button(self, text="2번셋팅", command = lambda: master.SwitchFrame(RPGPage2)).place(x=60, y=0, width=60, height=25)
        tk.Button(self, text="3번셋팅", state = tk.DISABLED).place(x=120, y=0, width=60, height=25)
        tk.Button(self, text="Back", command = lambda: master.SwitchFrame(Home)).place(x=440, y=0, width=60, height=25)



class FPSPage1(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.SaveButton = tk.Button(self, text = "save" ,command = lambda: SaveDB(3))
        self.SaveButton.place(x=255, y=340, width=40, height=25)
        self.Runbutton = tk.Button(self, text="run!",  command=lambda: RunGamepadLoop(self.Runbutton))
        self.Runbutton.place(x =205 , y =340,width = 40,height=25)
        self.MoveButton = tk.Button(self, text = "go" ,command = lambda: thread_sample())
        self.MoveButton.place(x=300, y=340, width=40, height=25)



##########################변수#############################


Tk_button = []      #게임패드 버튼객체가 담기는 배열
Tk_button_locate = [[70,170],[70,250],[30,210],[110,210],[50,70],
                    [410,70],[280,190],[330,190],[380,190],[430,190],
                    [280,240],[330,240],[380,240],[430,240]
]

BUTTON_BASKET = ""


##################DB부분###########################
#초기화


#이 프로그램 전체의 루프를 담당하는 변수. 신중히 다뤄줘요.
global GAMEPAD_LOOP
GAMEPAD_LOOP = False
ButtonBasket = []
KeySetting = []
keyIndex = [0,0,0,0,0,0,0,
            0,0,0,0,0,0,0]                  
KeyAmount = 14




##################메인#######################
if __name__ == "__main__":
    app = TkinerRoot()
    app.mainloop()
