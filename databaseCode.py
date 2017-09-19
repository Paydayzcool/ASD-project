#!/usr/bin/python3
import sqlite3
print("Content-type: text\n")
import cgi
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

con = sqlite3.connect('project.db')
cur = con.cursor()
print('a')
print(form['Function'].value)
print(form['test'].value)

def niceData(data):
    return(list(data[0]))
    
def newStudent(ID,fname,lname,classes):
    try:
        cur.execute('INSERT INTO Students VALUES(?,?,?)',(ID,fname,lname))
        classes = classes.split()
        for i in classes:
            cur.execute('INSERT INTO ReferenceStud (Student, Class) VALUES (?,?)',(ID, i))
        con.commit()
        return(True)
    except:
        print('error newStudent')
        con.rollback()
        return(False)


def newTeacher(ID, fname, lname, classes):
    try:
        cur.execute('INSERT INTO Teachers VALUES(?,?,?)',(ID,fname,lname))
        classes = classes.split()
        for i in classes:
            cur.execute('INSERT INTO ReferenceT VALUES(?,?)', (ID, i))
        con.commit()
        return(True)
    except:
        print('error newTeacher')
        con.rollback()
        con.close()
        return(False)

def newTask(Class,questions,answers,name):
    try:
        cur.execute('SELECT TaskID FROM TASKS WHERE Questions ="'+questions+'" AND Answers ="'+answers+'"')
        data = cur.fetchall()
        if len(data) == 0:
            cur.execute('INSERT INTO Tasks(Questions,Answers,Name, Classes) VALUES(?,?)',(questions,answers))
        
        cur.execute('SELECT Student FROM ReferenceStud WHERE Class = "'+Class + '"')
        data = cur.fetchall()
        data = niceData(data)
        cur.execute('SELECT TaskID FROM Tasks WHERE Questions = "'+questions+'" AND Answers = "'+answers+'"')
        ID = cur.fetchall()
        ID = int(ID[0][0])
        for i in range(len(data)):
            cur.execute('INSERT INTO Completion VALUES(?,?,?)',(ID,data[i],'N'))                   
        cur.execute('INSERT INTO refTasks VALUES(?,?,?)',(ID,Class,name))
        con.commit()
        return(True)
    except:
        print('error newTask')
        con.rollback()
        con.close()
        return(False)

def getTasks(ID):
    try:
        values = { "ID": ID }
        cur.execute('SELECT Task FROM Completion WHERE Student=:ID', values)
        data = cur.fetchall()
        data = niceData(data)
        tasks = []
        for i in data:
            cur.execute('SELECT Name FROM Tasks WHERE TaskID = '+str(i))
            temp = cur.fetchall()
            tasks.append(temp[0][0])
        return(tasks,data)
    except:
        print('error getTasks')
        con.rollback()
        con.close()
        return(False)

def getStudents(Class):
    try:
        cur.execute('SELECT Student FROM ReferenceStud WHERE Class = "'+Class+'"')
        students = cur.fetchall()
        students = niceData(students)
        return(students)
    except:
        print('Error getStudents')
        con.rollback()
        con.close()
        return('error')

def complete(student,task):
    try:
        cur.execute('UPDATE Completion SET Completed = "Y" WHERE Student = '+ str(student)+' AND Task = '+str(task))
        con.commit()
        return(True)
    except:
        print('error complete')
        con.rollback()
        con.close()
        return(False)

def getTask(ID):
    try:
        cur.execute('SELECT questions,answers FROM Tasks WHERE TaskID ='+str(ID))
        data = cur.fetchall()
        print(data)
        data = niceData(data)
        return(data)
    except:
        print('error getTask')
        con.rollback()
        con.close()
        return(False)

    
if form['Function'].value == 'NStudent':
    newStudent(int(form['ID'].value), form['fname'].value, form['lname'.value], form['classes'].value)
elif form['Function'].value == 'NTeacher':
	newTeacher(form['ID'].value, form['fname'].value, form['lname'].value, form['classes'].value)
elif form['Function'].value == 'NTask':
	newTask(form['Class'].value,form['Questions'].value,form['Answers'].value,form['name'].value)
elif form['Function'].value == 'GTasks':
	pass
elif form['Function'].value == 'GStudents':
	pass
elif form['Function'].value == 'Complete':
    pass
elif form['Function'].value == 'GTask':
    pass
con.close()
