from fastapi import FastAPI, HTTPException
from tasks import tasks

app = FastAPI()

'''api動作確認用
@app.get("/")
def read_root():
    return {"Hello": "World"}
'''

# GET
# タスク一覧を取得
@app.get("/todo/api/v1.0/tasks")
def get_tasklist():
    return {"data": tasks}

# タスクIDを指定して取得
@app.get("/todo/api/v1.0/tasks/{id}")
def get_task(id: Int):
    task_id = int(id)
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        raise HTTPException(status_code=404, detail="Not found")
    else:
        return {"data": task[0]}

# POST
# タスクの登録（パスはPOSTメソッドのボディ）
@app.post("/todo/api/v1.0/tasks")
def create_task(request_data: dict):
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request_data['title'],
        'description': request_data['description'],
        'done': False
    }
    tasks.append(task)
    return {"data": request_data}

# PATCH
# 既存タスクの更新
@app.patch("/todo/api/v1.0/tasks/{id}")
def patch_task(id: in, request_data: dict):
    task = [task for task in tasks if task['id'] == id]
    if len(task) == 0:
        raise HTTPException(status_code=404, detail="Not found")
    for key in request_data.key():
        task[0][key] = request_data[key]
    return {"data": tasks[0]}
