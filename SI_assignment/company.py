class Company(object):
    def __init__(self,name,field,type,CEO,coach):
            self.name=name
            self.field=field
            self.type=type
            self.CEO=CEO
            self.coach=coach
    def add(self):
        try:
            conn = sqlite3.connect('Company.db')
            c=conn.cursor()
            c.execute('''CREATE TABLE company
             (name text,field text,type text,CEO text,mentor_name text)''')
            name=input("Enter name ")
            field=input("Enter field")
            type=input("Enter type")
            CEO=input("Enter CEO")
            coach=input("Enter coach name ")
            c.execute("INSERT INTO student VALUES(name,field,type,CEO,mentor)")
            conn.commit()
        except:
            print ((sys.exc_info()[0]),"occured")
        else:
            print("successfully added")
        finally:
            conn.close()
