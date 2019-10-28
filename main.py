import psycopg2
from migrations import *
from config.config import conn_config

params = conn_config()
conn = psycopg2.connect(**params)
cur = conn.cursor()

def main():
    drop()
    create()
    insert()

    cur.close()
    conn.close()
    
    
if __name__ == '__main__':
    main()