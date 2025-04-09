#!/usr/local/bin/python
# Connect to MariaDB Platform
import mysql.connector #mariadb
from flask import session, redirect

import mysql.connector

# 建立與資料庫連線的函式
def get_connection():
    try:
        conn = mysql.connector.connect(
            user="root",
            password="",  # 若有密碼請填入
            host="localhost",
            port=3306,
            database="CO"
        )
        return conn
    except mysql.connector.Error as e:
        print(e)
        print("Error connecting to DB")
        exit(1)

# 取得所有記錄
def get_all_records():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM records ORDER BY date DESC")
    records = cursor.fetchall()
    cursor.close()
    conn.close()
    return records

# 新增記錄
def insert_records(records):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO records (type, amount, description, date) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (records['type'], records['amount'], records['description'], records['date']))
    conn.commit()
    cursor.close()
    conn.close()

# 刪除記錄
def delete_records(records_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM records WHERE id = %s", (records_id,))
    conn.commit()
    cursor.close()
    conn.close()


