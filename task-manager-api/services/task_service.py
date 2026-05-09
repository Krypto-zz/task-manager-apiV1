from models.task import Task
import bcrypt
from database.database import db_create, db_get, db_update, db_delete, db_register_user, db_get_user_by_username

def get_all_tasks():
    task_tupla = db_get()
    tasks_db = []
    for task in task_tupla:
        tasks_db.append(Task(id=task[0], title=task[1], completed=task[2]))
    
    print("Action taken")
    return tasks_db

def create_task(title : str):
    db_create(title)
    return {"message" : "Created task"}

def register_user(username: str, password_txt: str):
    pw_hash = password_txt.encode('utf-8')
    sal = bcrypt.gensalt()
    b_password_hash = bcrypt.hashpw(pw_hash, sal)
    password_hash_str = b_password_hash.decode('utf-8')
    try:
        db_register_user(username, password_hash_str)
        return {"message" : "User registered successfully"}
    except Exception as e:
        return {"error": "Username already taken or database error"}

def authenticate_user(username: str, password_txt: str):
    data_user = db_get_user_by_username(username)
    if data_user is not None:
        hash_bytes = data_user['password_hash'].encode('utf-8')
        password_bytes = bytes(password_txt, 'utf-8')

        if bcrypt.checkpw(password_bytes, hash_bytes):
            return {"message":"Authorized Access"}
    else:
        return {"message":"Access Denied"}

def update_task(id_objetivo : int, new_state : bool):
    db_update(id_objetivo, new_state)
    return {"message" : "Updated task"}

def delete_task(id_objetivo : int):
    db_delete(id_objetivo)
    return {"message" : "Deleted task"}
