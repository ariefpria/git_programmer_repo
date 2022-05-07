import Pymysql
import psycopg2 as pg
from config import config

def connect(filename, section):
    conn = None

    try:
        params = config(filename, section)
        print('connecting to {} database ...'.format(section))

    except(Exception) as error:
        print(error)
    finally:
        print('finnaly')
