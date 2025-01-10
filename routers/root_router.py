from fastapi import APIRouter

root_router = APIRouter(prefix="", tags=["root"])


@root_router.get("/")
def read_root():
    return "Welcome to ScriptGenie API"
