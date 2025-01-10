from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import title_router, root_router

app = FastAPI()

app.include_router(root_router)
app.include_router(title_router)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Run the server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5001)
