import sqlite3

def get_conn():
    conn = sqlite3.connect('lvsys/db/lv.db')
    return conn

def test_get_user(conn):
    cur = conn.cursor();
    cur.execute('select id, username, fullname, group_id, approver_id from user')
    return cur.fetchall()