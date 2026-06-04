from fastapi import FastAPI

from app.database.db import Base
from app.database.db import engine

from app.routes.auth import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Expense Tracker API"
)

app.include_router(auth_router)


@app.get("/")
def root():

    return {
        "message": "Expense Tracker API Running"
    }