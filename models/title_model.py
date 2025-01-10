from typing import Any
from pydantic import BaseModel

from models.response_model import ResponseModel


class ScriptRequestDTO(BaseModel):
    script: str


class ScriptResponseData(BaseModel):
    intro: str


class ScriptResponseDTO(ResponseModel[ScriptResponseData]):
    pass
