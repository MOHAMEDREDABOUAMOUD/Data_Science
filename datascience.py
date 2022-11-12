import csv
import mysql.connector as mysql
from matplotlib import pyplot as plt
import numpy as np
def afficher():
    try:
        db=mysql.connect(
            user='reda',
            password='1234',
            host='127.0.0.1',
            database='note'
        )
        cursor=db.cursor()
        cursor.execute("select * from etud")
        #cursor.execute("describe etud")
        dbs=cursor.fetchall()
        for result in dbs:
            print(result)
        cursor.close()
        db.close()
    except mysql.Error as e:
        print(e)
def select(requete):
    try:
        db=mysql.connect(
            user='reda',
            password='1234',
            host='127.0.0.1',
            database='note'
        )
        cursor=db.cursor()
        cursor.execute(requete)
        dbs=cursor.fetchall()
        data=[]
        for result in dbs:
            data.append(result)
        cursor.close()
        db.close()
        return data
    except mysql.Error as e:
        print(e)
def insert(id,name,email,annee,n):
    try:
        db=mysql.connect(
            user='reda',
            password='1234',
            host='127.0.0.1',
            database='note',
            autocommit=True
        )
        cursor=db.cursor()
        cursor.execute('INSERT INTO etud (id,name,email,annee,note) VALUES (%s,%s,%s,%s,%s)',(id,name,email,annee,n))
        cursor.close()
        db.close()
    except mysql.Error as e:
        print(e)
def export(file):
    with open(file,newline='') as f:
        rows=csv.reader(f,delimiter=',')
        for row in rows:
            insert(int(row[0]),row[1],row[2],int(row[3]),float(row[4]))
def getScoreByStudents(email):
    return select("select annee,note from etud where email like '"+email+"';")
def progress(email):
    #[(2020,16),(2021,17)]
    data=getScoreByStudents(email)
    plt.title(email)
    y=[]
    x=[]
    for item in data:
        y.append((item[1]))
        x.append((str(item[0])))
    plt.ylabel('MOYENNE')
    plt.xlabel('ANNEE')
    plt.plot(x,y,'g-s',label='progress')
    plt.show()
def freetable():
    try:
        db=mysql.connect(
            user='reda',
            password='1234',
            host='127.0.0.1',
            database='note',
            autocommit=True
        )
        cursor=db.cursor()
        cursor.execute("delete from etud where email like '%@%'")
        cursor.close()
        db.close()
    except mysql.Error as e:
        print(e)
freetable()
export("note.csv")
afficher()
print(getScoreByStudents('walid@gmail.com'))
progress('walid@gmail.com')