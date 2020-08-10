"""実行時エラー
python schema_test.pyが通らない
shcemas/__init__.pyの79行目で構文エラーが発生（pythonのバージョンに問題あり？）
"""
from pydantic import ValidationError
from schemas import TaskSchema

try:
    TaskSchema()

except ValidationError as e:
    print(e.json())
