from pydantic import BaseModel
import json
from typing import TypeVar, Generic
T = TypeVar('T')


class ResponseModel(BaseModel, Generic[T]):
    status: str
    message: str
    data: T

    def to_dict(self):
        return {
            "status": self.status,
            "message": self.message,
            "data": self.data
        }

    def to_json(self):
        return json.dumps(self.to_dict())

    def to_json_string(self):
        return json.dumps(self.to_dict(), indent=4)
