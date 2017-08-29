from sqlite3 import *
con = connect('project.db')
cur = con.cursor()

def newStudent(ID,fname,lname,classes):
    #try:
    cur.execute('INSERT INTO Students VALUES(?,?,?)',(ID,fname,lname))
    classes = classes.split()
    for i in classes:
        print(ID,i)
#       cur.execute('INSERT INTO ReferenceS (Student, Class) VALUES (?,?)',(ID, i))
        print('INSERT INTO ReferenceS (Student, Class) VALUES (' + str(ID) + ',"' + i + '")')
        cur.execute('INSERT INTO ReferenceS VALUES (' + str(ID) + ',"' + i + '")')
    con.commit()                        
    """except:
        print('error newStudent')
        con.rollback()"""


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
    try:
        cur.execute('SELECT TaskID FROM TASKS WHERE Questions =',questions,'AND Answers =',answers)
        data = cur.fetchall()
        if data.len() == 0:
            cur.execute('INSERT INTO Tasks VALUES(?,?,?,?)',(questions,answers,name))
        
        cur.execute('SELECT Student FROM ReferenceS WHERE Class =',Class)
        data = cur.fetchall()
        print(data)
        cur.execute('SELECT TaskID FROM Tasks WHERE Questions =',questions,'AND', 'Answers =',answers)
        ID = cur.fetchall()
        print(ID)
        for student in data:
            cur.execute('INSERT INTO Completion VALUES(?,?,?)',(student,ID,'N'))
            
        con.commit()                        
    except:
        print('error newTask')
        con.rollback()

newStudent(1083698, 'Coen', 'Heyning', '10MSA02') 
con.commit()
con.close()
