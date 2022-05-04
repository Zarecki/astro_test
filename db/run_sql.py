import sqlite3
import os

def db_connection():
    path = os.path.dirname(os.path.abspath(__file__))
    db = os.path.join(path, "./nasa_facilities.db")
    conn = sqlite3.connect(db)
    conn.execute("PRAGMA foreign_keys = 0")
    conn.row_factory = sqlite3.Row 
    return conn

def sql_runner(statement, values = []):
    db = db_connection()
    cursor = db.cursor()
    results = cursor.execute(statement, values)
    results = cursor.fetchall()
    db.commit()
    db.close()
    return results
