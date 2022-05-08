import mysql.connector as mysql
import psycopg2 as pg
from config import config

def connect(filename, section):
    conn = None
    
    try:
        params = config(filename, section)
        
        if section = "mysql":
            conn = mysql.connect(**params)
        else:
            conn = pg.connect(**params)

    except(Exception, mysql.DatabaseError) as error:
        print(error)
    finally:
        print("finally")

def setIC_Data():
    stmt = "select * from redcap_data where project_id = 16"

    conn, cur = connect('database', 'mysql')

def setCC_Data():
    stmt = "select * from redcap_data where project_id = 17"
    conn, cur = connect('database', 'mysql')

