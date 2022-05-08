import pymysql

def connect(filename, section):
    conn = None

    try:
        params = config(filename, section)

    except(Exception) as error:
        print(error)
    finally:
        print("finaal")

def setIC_Data():
    stmt = "select * from redcap_data where project_id = 16"

    conn = connect('database','mysql')
