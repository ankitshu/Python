import mysql.connector
from mysql.connector import errorcode

class DBExample:
    cnx=None
    
    def __init__(self,u_name, passwd, host_name, db):
        self.createConnection(u_name, passwd, host_name, db)
        
        
    def createConnection(self,u_name,passwd,host_name,db):
        DBExample.cnx = mysql.connector.connect(user=u_name, password=passwd,host=host_name,database=db)
        #cnx.close()
    
    def createCursor(self):
        return DBExample.cnx.cursor(buffered=True)
    
    def insertData(self,t,cur):
        sql="INSERT INTO employee(f_name,l_name, age, id) VALUES (%s,%s,%s,%s)"
        #sql="INSERT INTO employee(f_name,l_name, age, id) VALUES ("+f_name,l_name,age,id+")"
        cur.execute(sql,t)
        self.cnx.commit()
    
    def getData(self,cur):
        sql='select * from employee'
        cur.execute(sql)
        results=cur.fetchall()
        print(type(results))
        print(results)
        for row in results:
            print(type(row))
            f_name=row[0]
            l_name=row[1]
            age=row[2]
            empId=row[3]
            print(f_name,l_name,age,empId)

    
    def updateRecord(self,cur,sql):
        print(sql)
        cur.execute(sql)
        self.cnx.commit()
                

    def getSingleRecord(self,cur):
        sql='select * from employee'
        cur.execute(sql)
        result=cur.fetchone()
        print(type(result))
        f_name=result[0]
        l_name=result[1]
        age=result[2]
        empId=result[3]
        print('--->',f_name,l_name,age,empId)
        #print(results)    

conn=DBExample('root','password','localhost','company')
cur=conn.createCursor()
# f_name='Yogesh'
# l_name='Chandna'
# age=25
# empId='1002'
# t=(f_name,l_name,age,empId)
# print('Insert data')
# conn.insertData(t, cur)
# conn.insertData(('puneet','singh','25','1003'), cur)
# print('Data inserted successfully')
# exit(0)


# print("read single record")
# conn.getSingleRecord(cur)
# print("read record successfully")
# #exit(0)
# 
# print("read data")
# conn.getData(cur)
# print("read data successfully")
# exit(0)

# print('update data')
# conn.updateRecord(cur, 'update employee set age = age + 10 where l_name = "Sharma"')
# print('updated successfully')
# exit(0)

# print('delete data')
# conn.updateRecord(cur, "delete from employee where age ='%d'" %(36))
# print('deleted successfully')
# exit(0)








#create schema
DB_NAME = 'company_db'

TABLES = {}
TABLES['person'] = (
    "CREATE TABLE `employees` ("
    "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
    "  `birth_date` date NOT NULL,"
    "  `first_name` varchar(14) NOT NULL,"
    "  `last_name` varchar(16) NOT NULL,"
    "  `gender` enum('M','F') NOT NULL,"
    "  `hire_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`)"
    ")")

TABLES['departments'] = (
     "CREATE TABLE `departments` ("
    "  `dept_no` char(4) NOT NULL,"
    "  `dept_name` varchar(40) NOT NULL"
    ")")


def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    DBExample.cnx.database = DB_NAME  
except mysql.connector.Error as err:
    print('Error')
    print(err.args)
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        print('IF')
        create_database(cur)
        conn.cnx.database = DB_NAME 
    else:
        print(err)
        exit(1)



for name, ddl in TABLES.items():
    #print(ddl)
    try:
        print("Creating table {}: ".format(name))
        cur.execute(ddl)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err)
    else:
        print("OK")

cur.close()
conn.cnx.close()

#DBExample.cnx.close()






    
    
