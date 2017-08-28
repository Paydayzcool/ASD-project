from sqlite3 import *
con = connect('project.db')
cur = con.cursor()

def newStudent(ID,fname,lname,classes):
    try:
        cur.execute('INSERT INTO Students VALUES(?,?,?)',(ID,fname,lname))

        classes = classes.split()
        for i in classes:
            cur.execute('INSERT INTO ReferenceS VALUES(?,?)', (ID, i))
    
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


con.commit()
con.close()
