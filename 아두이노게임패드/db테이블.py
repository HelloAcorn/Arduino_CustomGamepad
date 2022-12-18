import sqlite3


con = sqlite3.connect('Keyarray.db')
cursor = con.cursor()
sql = "insert into KeyTable2 values ('1','2','3','4','5','6','7','8','9','0','f1','f2','f3','f4')"
cursor.execute(sql)
cursor.execute("commit")
