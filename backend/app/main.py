from fastapi import FastAPI

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

app.include_router(auth_router)

app.include_router(expense_router)


@app.get("/")
def root():

    return {
        "message": "Expense Tracker API Running"
    }