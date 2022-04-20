import sqlalchemy as sql
import pandas as pd
# import sqlite3
import os
print (os.getcwd())
path = "sqlite:///"+os.getcwd() + "/test1.db"
db = sql.create_engine(path)
#db2 = sqlite3.connect(path)
#pointer = db2.cursor()
# try:

#     pointer.execute("CREATE TABLE test1 (test_id INTEGER PRIMARY KEY, name TEXT NOT NULL,email TEXT NOT NULL UNIQUE);")
# except:
#     print('[TABLE EXISTS ALREADY]')
try:
    pd.read_sql_query("CREATE TABLE test2 (test_id INTEGER PRIMARY KEY, name TEXT NOT NULL,email TEXT NOT NULL UNIQUE);", db)
except:
    print ("[Table already exists]")
print(pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", db))

# pd.read_sql("CREATE TABLE test2 (test_id INTEGER PRIMARY KEY, name TEXT NOT NULL,email TEXT NOT NULL UNIQUE);", db)
# pointer.execute("SELECT name FROM sqlite_master WHERE type='table';")
# print(pointer.fetchall())


