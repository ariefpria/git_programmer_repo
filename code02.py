import Pymysql

def connect(filename, section):
    conn = None

    try:
        params = config(filename, section)

    except(Exception) as error:
        print(error)
    finally:
        print('finnaly')
