from fastapi import FastAPI, HTTPException
from tasks import tasks

app = FastAPI()

'''api動作確認用
@app.get("/")
def read_root():
    return {"Hello": "World"}
'''

@app.get("/todo/api/v1.0/tasks")
def get_tasklist():
    return {"data": tasks}