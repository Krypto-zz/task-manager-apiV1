import sqlite3

PATH_DB = r'D:\BASE_DE_DATOS_tasks\task.db'
#CONECTION DATABASE
def connect_db():
    return sqlite3.connect(PATH_DB)

#CREATE
def db_create(task):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO task(title) VALUES(?)", (task,))
    conn.commit()
    conn.close()

#REGISTER USER
def db_register_user(username, password_hash):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERt INTO users(username, password_hash) VALUES (?, ?)", (username, password_hash))
    conn.commit()
    conn.close()

#LOGIN USER
def db_get_user_by_username(username):
    conn = connect_db()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    
    data_user = cursor.fetchone()
    if data_user != None:
        return dict(data_user)
    else:
        return None
#GET
def db_get():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM task")
    data = cursor.fetchall()
    conn.close()
    return data

#UPDATE
def db_update(id_task, completed):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE task SET completed = ? WHERE id= ?", (completed, id_task))
    conn.commit()
    conn.close()

#DELETE
def db_delete(id_task):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM task WHERE id = ?", (id_task,))
    conn.commit()
    conn.close()

