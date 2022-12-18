import keyboard
import serial
import threading
import time
import tkinter
from tkinter import messagebox
import sqlite3


################메모장############################
'''
ARDUINO.isOpen() : 포트가 열려 있는지 확인합니다. return값 true false
ARDUINO.open() : 포트를 열고 '. 
ARDUINO.close() : 포트를 닫습니다. 




'''
####################함수선언#######################
def ConnectDB():
    con = sqlite3.connect('Keyarray.db')
    cursor = con.cursor()
    return cursor


def thread_sample():
    global GAMEPAD_LOOP
    while GAMEPAD_LOOP == True:
        try:
            communicate_arduino = ARDUINO.readline()
            input_key = communicate_arduino[1:15]
            SetPressAndRelease(input_key)
            UpdateKeyIndex(input_key)
        except:
            GAMEPAD_LOOP = False
            messagebox.showwarning("경고", "선이 빠저버렸습니다.")
        
def UpdateKeyIndex(input_key):
    for i in range(14):
        if input_key[i:i+1] == b'1':
            keyIndex[i] = 1
        elif input_key[i:i+1] == b'0':
            keyIndex[i] = 0
    
def SetPressAndRelease(input_key):
    for i in range(14):
        if input_key[i:i+1] == b'1' and keyIndex[i] == 0:
            keyboard.press(KeySetting[i])
        if input_key[i:i+1] == b'0' and keyIndex[i] == 1:
            keyboard.release(KeySetting[i])

def RunGamepadLoop():
    global GAMEPAD_LOOP
    if GAMEPAD_LOOP == False:
        GAMEPAD_LOOP = True
        ARDUINO.open()
        gamepad_loop_thread = threading.Thread(target = thread_sample)
        gamepad_loop_thread.start()
        Runbutton.configure(text = "stop")
    else:
        GAMEPAD_LOOP = False
        ARDUINO.close()
        Runbutton.configure(text = "run!")


def ChangeKey():
    cur = ConnectDB()
    CreateNewWindow()

def CreateNewWindow():
    newWindow = tkinter.Toplevel(window)
    label = tkinter.Label(newWindow, text = "New Window")
    button = tkinter.Button(newWindow, text = "New Window button")

    label.pack()
    button.pack()


    
##################DB부분###########################
#초기화
KeySetting = []
keyIndex = [0,0,0,0,0,0,0,
            0,0,0,0,0,0,0]
KeyAmount = 14


cur = ConnectDB()

sql = "select * from keytable1"

cur.execute(sql)
db_keysetting = cur.fetchall()
for i in range(KeyAmount):
    KeySetting.append(db_keysetting[0][i])

cur.close()

###############변수 및 함수 선언####################


#이 프로그램 전체의 루프를 담당하는 변수. 신중히 다뤄줘요.
global GAMEPAD_LOOP
GAMEPAD_LOOP = False




#아두이노와 파이썬 시리얼 연결
try:
    ARDUINO = serial.Serial("com3", 9600, timeout=1,
                                xonxoff=False, rtscts=False, dsrdtr=False)
    ARDUINO.close()
except :
    pass


    
########################tkinter##################################
            
Tk_button = []      #게임패드 버튼객체가 담기는 배열
Tk_button_locate = [[70,170],[70,250],[30,210],[110,210],[50,70],
                    [410,70],[280,190],[330,190],[380,190],[430,190],
                    [280,240],[330,240],[380,240],[430,240]
]


window=tkinter.Tk()
window.title("키세팅")
window.geometry("500x300+300+300")
window.resizable(False, False)

frame1 = tkinter.Frame(window)

for i in range(14):
    button = tkinter.Button(frame1, text=KeySetting[i],  command=lambda: ChangeKey())
    button.place(x = Tk_button_locate[i][0], y = Tk_button_locate[i][1],width = 40,height=30)
    Tk_button.append(button)

Runbutton = tkinter.Button(frame1, text="run!",  command=lambda: RunGamepadLoop())
Runbutton.place(x =220 , y =135,width = 60,height=30)
frame1.place(x=0, y=0,width=500, height=300)
window.mainloop()


####################게임패드(메인..?)#############################



