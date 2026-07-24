import datetime
from reports import get_total_spent


def get_expenses_by_month(month, expenses):
    return [exp for exp in expenses if exp["date"][:7] == month]


def get_current_month_total(expenses):
    current_month = datetime.date.today().strftime("%Y-%m")
    monthly_expenses = get_expenses_by_month(current_month, expenses)
    return get_total_spent(monthly_expenses)


def calculate_remaining_budget(budget, expenses):
    total_spent = get_current_month_total(expenses)
    return budget.get("monthly_budget", 0) - total_spent


def calculate_budget_percentage(monthly_budget, expenses):
    total_spent = get_current_month_total(expenses)
    if monthly_budget <= 0:
        return 0.0
    return (total_spent / monthly_budget) * 100


def calculate_budget_excess(monthly_budget, expenses):
    total_spent = get_current_month_total(expenses)
    if total_spent > monthly_budget:
        return total_spent - monthly_budget
    return 0
