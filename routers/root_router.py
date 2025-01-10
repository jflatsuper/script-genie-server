from fastapi import APIRouter

root_router = APIRouter(prefix="", tags=["root"])


@root_router.get("/")
def read_root():
    return {"Hello": "World"}
