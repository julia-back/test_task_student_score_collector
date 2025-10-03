import uvicorn
from fastapi import FastAPI
from scores.routers import router as scores_router
from users.routers import router as users_router


app = FastAPI()
app.include_router(scores_router)
app.include_router(users_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
