from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database.db import get_db
from app.database.models import Expense

from app.schemas.expense import (
    ExpenseCreate
)

from app.auth.jwt_handler import (
    get_current_user
)

router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"]
)


@router.post("/")
def create_expense(
    expense: ExpenseCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    new_expense = Expense(
        title=expense.title,
        amount=expense.amount,
        category=expense.category,
        description=expense.description,
        user_id=current_user["user_id"]
    )

    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)

    return new_expense


@router.get("/")
def get_expenses(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    expenses = (
        db.query(Expense)
        .filter(
            Expense.user_id
            == current_user["user_id"]
        )
        .all()
    )

    return expenses


@router.get("/{expense_id}")
def get_expense(
    expense_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    expense = (
        db.query(Expense)
        .filter(
            Expense.id == expense_id,
            Expense.user_id
            == current_user["user_id"]
        )
        .first()
    )

    if not expense:

        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    return expense


@router.put("/{expense_id}")
def update_expense(
    expense_id: int,
    updated_expense: ExpenseCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    expense = (
        db.query(Expense)
        .filter(
            Expense.id == expense_id,
            Expense.user_id
            == current_user["user_id"]
        )
        .first()
    )

    if not expense:

        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    expense.title = updated_expense.title
    expense.amount = updated_expense.amount
    expense.category = updated_expense.category
    expense.description = updated_expense.description

    db.commit()
    db.refresh(expense)

    return expense


@router.delete("/{expense_id}")
def delete_expense(
    expense_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    expense = (
        db.query(Expense)
        .filter(
            Expense.id == expense_id,
            Expense.user_id
            == current_user["user_id"]
        )
        .first()
    )

    if not expense:

        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    db.delete(expense)
    db.commit()

    return {
        "message": "Expense deleted successfully"
    }