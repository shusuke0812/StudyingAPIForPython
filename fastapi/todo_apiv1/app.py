from fastapi import FastAPI, HTTPException, BackgroundTasks
from task import tasks
from time import sleep
from datetime import datetime
from pydantic import BaseModel

class Task(BaseModel):
    title: str
    description: str = None
    done: bool = False

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
def get_task(id: int):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        raise HTTPException(status_code=404, detail="Not found")
    else:
        return {"data": task[0]}

# POST
# タスクの登録（パスはPOSTメソッドのボディ）
@app.post("/todo/api/v1.0/tasks")
def create_task(request_data: dict):
    """
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request_data['title'],
        'description': request_data['description'],
        'done': False
    }
    tasks.append(task)
    return {"data": request_data}
    """

    tasks.append(request_data)
    return {"data": request_data}

# PATCH
# 既存タスクの更新
@app.patch("/todo/api/v1.0/tasks/{id}")
def patch_task(id: int, request_data: dict):
    task = [task for task in tasks if task['id'] == id]
    if len(task) == 0:
        raise HTTPException(status_code=404, detail="Not found")
    for key in request_data.key():
        task[0][key] = request_data[key]
    return {"data": tasks[0]}

# DELETE
# タスクの削除
@app.delete("/todo/api/v1.0/tasks/{id}")
def delete_task(id: int):
    task = [task for task in tasks if task['id' == id]]
    if len(task) == 0:
        raise HTTPException(status_code=404, detail="Not found")
    task.remove(task[0])
    return {"result": "OK"}

# 非同期処理の例
# 時間のかかる処理をバックグラウンドで実行する
def slow_task(numbers: int):
    sleep(numbers)
    print(f'sleep done. {datetime.utcnow()}')

@app.get("/{numbers}")
async def backjobs(numbers: int, background_tasks: BackgroundTasks):
    background_tasks.add_task(slow_task, numebrs)
    return {"result": f"finish {datetime.utcnow()}"}