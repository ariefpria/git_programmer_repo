import mysql.connector as mysql

def connect(filename, section):
    conn = None

    try:
        print('Connecting to database')
    except:
        print(error)
    finally:
        print('final')

def set CC_Data():
    stmt1 = "select * from redcap_data where project_id = 17"
