import sqlite3
from sqlite3 import Error
import re
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        createTestCaseLog(conn)
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def createTestCaseLog(conn):
    database = r".DB"
 
    sql_create_table = """ CREATE TABLE IF NOT EXISTS test_case_log (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        context text,
                                        lines text,
                                        file text
                                    ); """
 
    # create tables
    if conn is not None:
        create_table(conn, sql_create_table)
    else:
        print("Error! cannot create the database connection.")

 
def insertSqliteTable(array):
    try:
        conn = create_connection(".DB")
        cursor = conn.cursor()
        sql ="""insert into test_case_log(context,lines,file) values """#salary = 10000 where id = 4"""
        for tuple in array:
            sql +="('"+tuple[0]+"','"+tuple[1]+"','" + re.escape(tuple[2])+"'),"

        sql=sql[:-1]
        print (sql)
        cursor.execute(sql)
        conn.commit()
        print("Record Inserted successfully ")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert sqlite table", error)
    finally:
        if (conn):
            conn.close()
            #print("The SQLite connection is closed")

 
def updateSqliteTable(array):
    try:
        conn = create_connection(".DB")
        cursor = conn.cursor()
        sql = ""
        for tuple in array:
            sql="Update test_case_log set lines = '"+tuple[1]+"',file = '" + tuple[2] +"'  where context = "+"'"+tuple[0]+"';"
            cursor.execute(sql)
        print (sql)
        
        conn.commit()
        print("Record Updated successfully ")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if (conn):
            conn.close()
            #print("The SQLite connection is closed")

 

def getLogs(file=""):
    rows=[]
    
   
    #file="C:\Users\arsen\Desktop\porc\Kod.py"
    #file=""
    print(file)
    try:
        conn = create_connection(".DB")
        cur = conn.cursor()
        sql = "SELECT * FROM test_case_log "
        if file:
            sql+="where file = '"+ file+"'"
        print(sql)
        cur.execute(sql)
 
        rows = cur.fetchall()
        #print(rows)
        #for row in rows:
            #print(row)
        cur.close()
    except sqlite3.Error as error:
        print("Failed to select sqlite table", error)
    finally:
        if (conn):
            conn.close()
            #print("The SQLite connection is closed")
    return rows