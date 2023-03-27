import numpy as np
import psycopg2

def connect_db():
    conn_string = "host='localhost' dbname='postgres' user='postgres' password='postgres'"
  # print the connection string we will use to connect
    print("Connecting to database\n  ->%s" % (conn_string))

  # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

  # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    print("Connected!\n")

connect_db()
