from fastapi import APIRouter
from models.task import Task, UserAuth

from services.task_service import get_all_tasks, create_task, update_task, delete_task, register_user, authenticate_user

router = APIRouter()
#GET
@router.get("/task")
def get_task():
    return get_all_tasks()

#REGISTER USER
@router.post("/register")
def post_new_user(user : UserAuth):
    return register_user(user.username, user.password)

#POST LOGIN
@router.post("/login")
def get_user_login(user : UserAuth):
    return authenticate_user(user.username, user.password)
#POST
@router.post("/task")
def post_task(task_data : Task ):
    return create_task(task_data.title)
    
#PUT
@router.put("/task/{id_obj}/{new_state}")
def put_task(id_obj : int, new_state : bool):
    return update_task(id_obj, new_state)

#DELETE
@router.delete("/task/{id_obje}")
def del_taks(id_obje : int):
    return delete_task(id_obje)