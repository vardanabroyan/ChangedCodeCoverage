import sqlite3
from sqlite3 import Error

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
                                        lines text
                                    ); """
 
    # create tables
    if conn is not None:
        create_table(conn, sql_create_table)
    else:
        print("Error! cannot create the database connection.")

 
def insertSqliteTable(dict):
    try:
        conn = create_connection(".DB")
        cursor = conn.cursor()
        sql ="""insert into test_case_log(context,lines) values """#salary = 10000 where id = 4"""
        for key in dict:
            sql +="('"+key+"','"+dict[key]+"'),"

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

 
def updateSqliteTable(dict):
    try:
        conn = create_connection(".DB")
        cursor = conn.cursor()
        sql = ""
        for key in dict:
            sql="Update test_case_log set lines = '"+dict[key]+"' where context = "+"'"+key+"';"
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

 

def getLogs():
    rows=[]
    try:
        conn = create_connection(".DB")
        cur = conn.cursor()
        cur.execute("SELECT * FROM test_case_log")
 
        rows = cur.fetchall()
 
        for row in rows:
            print(row)
        cur.close()
    except sqlite3.Error as error:
        print("Failed to select sqlite table", error)
    finally:
        if (conn):
            conn.close()
            #print("The SQLite connection is closed")
    return rows