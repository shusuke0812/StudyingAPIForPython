from fastapi import FastAPI, HTTPException
from tasks import tasks

app = FastAPI()

'''api動作確認用
@app.get("/")
def read_root():
    return {"Hello": "World"}
'''

# タスク一覧を取得
@app.get("/todo/api/v1.0/tasks")
def get_tasklist():
    return {"data": tasks}

# タスクIDを指定して取得
@app.get("/todo/api/v1.0/tasks/{id}")
def get_task(id):
    task_id = int(id)
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        raise HTTPException(status_code=404, detail="Not found")
    else:
        return {"data": task[0]}