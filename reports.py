def get_category_totals(expenses):
    totals = {}
    for exp in expenses:
        category = exp["category"]
        totals[category] = totals.get(category, 0) + exp["amount"]
    return dict(sorted(totals.items()))


def get_extreme_expenses(expenses, mode="highest"):
    if not expenses:
        return []
    reverse = mode == "highest"
    sorted_expenses = sorted(expenses, key=lambda x: x["amount"], reverse=reverse)
    target_amount = sorted_expenses[0]["amount"]
    extreme_expenses = []
    for exp in sorted_expenses:
        if exp["amount"] == target_amount:
            extreme_expenses.append(exp)
        else:
            break
    return extreme_expenses


def get_total_spent(expenses):
    return sum(exp["amount"] for exp in expenses)


def get_average_expense(expenses):
    total = get_total_spent(expenses)
    count = len(expenses)
    return total / count if count > 0 else 0


def get_highest_amount(expenses):
    return max(exp["amount"] for exp in expenses)


def get_lowest_amount(expenses):
    return min(exp["amount"] for exp in expenses)


def get_summary(expenses):
    total_spent = get_total_spent(expenses)
    average = get_average_expense(expenses)
    highest_expense = get_highest_amount(expenses)
    lowest_expense = get_lowest_amount(expenses)
    return {
        "total_expenses": len(expenses),
        "total_spent": total_spent,
        "average_expense": average,
        "highest_expense": highest_expense,
        "lowest_expense": lowest_expense,
    }
