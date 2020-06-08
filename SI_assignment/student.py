import sqlite3
from person import Person
class Student(Person):
    def add(self):
        try:
            conn = sqlite3.connect('Student.db')
            c=conn.cursor()
            c.execute('''CREATE TABLE student
             (name text, age int, gender text, contact text,college text,branch text ,CGPA real,email text)''')
            name=input("Enter name ")
            age=input("Enter age")
            gender=input("Enter gender")
            contact=input("Enter contact")
            college=input("Enter college ")
            branch=input("Enter branch")
            CGPA=input("Enter CGPA")
            email=input("Enter email")
            c.execute("INSERT INTO student VALUES(name,age,gender,contact,college,branch,CGPA,email)")
            conn.commit()
        except:
            print ((sys.exc_info()[0]),"occured")
        else:
            print("successfully added")
        finally:
            conn.close()