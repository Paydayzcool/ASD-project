import sqlite3
con = sqlite3.connect('project.db')
cur = con.cursor()
def niceData(data):
    outData = []
    for i in range(len(data)):
        outData.append(data[i][0])
    return(outData)
    
def newStudent(ID,fname,lname,classes):
    try:
        cur.execute('INSERT INTO Students VALUES(?,?,?)',(ID,fname,lname))
        classes = classes.split()
        for i in classes:
            cur.execute('INSERT INTO ReferenceStud (Student, Class) VALUES (?,?)',(ID, i))
        con.commit()
        return('success')
    except:
        print('error newStudent')
        con.rollback()
        return('error')


def newTeacher(ID, fname, lname, classes):
    try:
        cur.execute('INSERT INTO Teachers VALUES(?,?,?)',(ID,fname,lname))
        classes = classes.split()
        for i in classes:
            cur.execute('INSERT INTO ReferenceT VALUES(?,?)', (ID, i))
    
        con.commit()
        return('success')
    except:
        print('error newTeacher')
        con.rollback()
        return('error')

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
        return('success')
    
    except:
        print('error newTask')
        con.rollback()
        return(error)

def getTasks(ID):
    try:
        print('SELECT Task FROM Completion WHERE Student =',ID)
        values = { "ID": ID }
        cur.execute('SELECT Task FROM Completion WHERE Student=:ID', values)
        data = cur.fetchall()
        data = niceData(data)
        tasks = []
        for i in data:
            cur.execute('SELECT Name FROM Tasks WHERE TaskID = '+i)
            temp = cur.fetchall()
            tasks.append(temp[0][0])
        return(tasks,data)
        
    except:
        print('error getTasks')
        con.rollback()
        return('error')

def getStudents(Class):
    try:
        cur.execute('SELECT Student FROM ReferenceStud WHERE Class = "'+Class+'"')
        students = cur.fetchall()
        students = niceData(students)
        return(students)
    except:
        print('Error getStudents')
        con.rollback()

def complete(student,task):
    try:
        cur.execute('UPDATE Completion SET Completed = "Y" WHERE Student = '+ str(student)+' AND Task = '+str(task))
        con.commit()
        return(True)
    except:
        print('error complete')
        con.rollback()
        return(False)

def getTask(ID):
    try:

    except:
con.commit()
con.close()
