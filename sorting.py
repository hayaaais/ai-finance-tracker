def sort_expenses(expenses, field, reverse):
    return sorted(expenses, key=lambda x: x[field], reverse=reverse)
