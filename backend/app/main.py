from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.db import (
    Base,
    engine
)

from app.routes.auth import (
    router as auth_router
)

from app.routes.expenses import (
    router as expense_router
)

Base.metadata.create_all(
    bind=engine
)

app = FastAPI(
    title="Expense Tracker API",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_router)

app.include_router(expense_router)


@app.get("/")
def root():

    return {
        "message": "Expense Tracker API Running"
    }