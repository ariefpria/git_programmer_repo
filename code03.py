import pymysql
import psycopg2 as pg
from config import config

def connect(filename, section):
    conn = None
    print('connecting to {} database ...'.format(section))

    try:
        params = config(filename, section)

    except(Exception) as error:
        print(error)
    finally:
        print("finaal")

def setIC_Data():
    stmt = "select * from redcap_data where project_id = 16"

    conn = connect('database','mysql')
