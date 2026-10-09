from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import db
from routes import auth

@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.connect()
    yield
    await db.disconnect()

app = FastAPI(lifespan=lifespan)

app.include_router(auth.router, prefix="/auth")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Habit Tracker API"}