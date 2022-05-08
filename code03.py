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
        print("final')
