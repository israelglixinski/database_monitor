
from dotenv import load_dotenv
import oracledb
import os



load_dotenv() 
ORACLE_HOST = os.getenv('ORACLE_HOST')
ORACLE_PORT = os.getenv('ORACLE_PORT')
ORACLE_BASE = os.getenv('ORACLE_BASE')
ORACLE_USER = os.getenv('ORACLE_USER')
ORACLE_PASS = os.getenv('ORACLE_PASS')



def connect():
    conn = oracledb.connect(
        user=ORACLE_USER
        , password=ORACLE_PASS
        , dsn=f"{ORACLE_HOST}:{ORACLE_PORT}/{ORACLE_BASE}"
        )
    return conn

def test_connection():
    conn = connect()
    cur = conn.cursor()
    cur.execute("select systimestamp from dual")
    return cur.fetchall()

if __name__ == "__main__":
    print (test_connection())
    pass

