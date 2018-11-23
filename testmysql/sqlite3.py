import sqlite3 as lite

conn = lite.connect('nima.db')
curs = conn.cursor()

def createTable():
    curs.execute("CREATE TABLE nima(Language VARCHAR, Version REAL, Skill TEXT)")
def enterData(var1, var2, var3):
    curs.execute("INSERT INTO nima VALUES(?, ?, ?)", (var1, var2, var3))
    conn.commit()
def readAll():
    for row in curs.execute("SELECT * FROM nima"):
        print(row)
        print(row[0])
enterData("Python", 2.2, "Bsc")
readAll()
conn.close()