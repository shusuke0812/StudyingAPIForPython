from pydantic import ValidationError
from schemas import TaskSchema

try:
    TaskSchema()

except ValidationError as e:
    print(e.json())
