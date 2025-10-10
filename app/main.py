import uvicorn
from fastapi import FastAPI
from scores.routers import router as scores_router
from users.routers import router as users_router
from auth.routers import router as auth_router
from config import settings
from contextlib import asynccontextmanager
from database import db_manager
import logging
from logging_config import logging_queue_listener


logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(fastapi_app: FastAPI):
    logging_queue_listener.start()
    logger.info("Start FastAPI application.")
    yield
    logger.info("Stop FastAPI application.")
    await db_manager.dispose_engine()
    logger.info("Stop database engine.")
    logging_queue_listener.stop()


app = FastAPI(lifespan=lifespan)
app.include_router(scores_router)
app.include_router(users_router)
app.include_router(auth_router)


if __name__ == "__main__":
    uvicorn.run("main:app",
                host=settings.run.host,
                port=settings.run.port,
                reload=True)
