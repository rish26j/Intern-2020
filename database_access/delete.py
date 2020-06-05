import pymysql

db = pymysql.connect("localhost","testuser","testxyz")

cursor = db.cursor()

sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (60)
try:
   cursor.execute(sql)
   db.commit()
except:
   db.rollback()
db.close()