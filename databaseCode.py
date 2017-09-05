import sqlite3
con = sqlite3.connect('project.db')
cur = con.cursor()
def newStudent(ID,fname,lname,classes):
    try:
        cur.execute('INSERT INTO Students VALUES(?,?,?)',(ID,fname,lname))
        classes = classes.split()
        for i in classes:
            cur.execute('INSERT INTO ReferenceStud (Student, Class) VALUES (?,?)',(ID, i))
        con.commit()                       
    except:
        print('error newStudent')
        con.rollback()


def newTeacher(ID, fname, lname, classes):
    try:
        cur.execute('INSERT INTO Teachers VALUES(?,?,?)',(ID,fname,lname))
        classes = classes.split()
        for i in classes:
            cur.execute('INSERT INTO ReferenceT VALUES(?,?)', (ID, i))
    
        con.commit()                        
    except:
        print('error newTeacher')
        con.rollback()

def newTask(Class,questions,answers,name):
    #try:
        cur.execute('SELECT TaskID FROM TASKS WHERE Questions ="'+questions+'" AND Answers ="'+answers+'"')
        data = cur.fetchall()
        if len(data) == 0:
            cur.execute('INSERT INTO Tasks(Questions,Answers,Name) VALUES(?,?,?)',(questions,answers,name))
        
        cur.execute('SELECT Student FROM ReferenceStud WHERE Class = "'+Class + '"')
        data = cur.fetchall()
        data = list(data[0])
        print(data)
        cur.execute('SELECT TaskID FROM Tasks WHERE Questions = "'+questions+'" AND Answers = "'+answers+'"')
        ID = cur.fetchall()
        ID = list(ID[0])
        print(ID)
        for i in range(len(data)):
            cur.execute('INSERT INTO Completion VALUES(?,?,?)',(data[i],ID[i],'N'))
            
        con.commit()                        
        '''except:
        print('error newTask')
        con.rollback()'''

def getTasks(ID, Class):
    try:
        cur.execute('SELECT ID FROM Completion WHERE student =',ID)
        taskIDs = cur.fetchall()
        tasks = []
        for task in taskIDs:
            cur.execute('SELECT name FROM Tasks WHERE ID =',task)
            tasks.append(cur.fetchall())
        return(tasks)
    except:
        print('error getTasks')
        con.rollback()

def getStudents(Class):
    try:
        cur.execute('SELECT Student FROM ReferenceS WHERE Class =',Class)
        students = cur.fetchall()
        return(students)
    except:
        print('Error getStudents')
        con.rollback()

def complete(student,task):
    try:
        cur.execute('Completion SET Complete = "Y" WHERE Student =', student,'AND Task =',task)
        con.commit()
    except:
        print('error complete')
        con.rollback()
newTask('10MSA02', '10+1 11+2', '11 13', 'Basic Addition')
con.commit()
con.close()
