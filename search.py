import datetime


def filter_by_category(expenses, category):
    return [exp for exp in expenses if exp["category"] == category]


def filter_by_date(expenses, date):
    return [exp for exp in expenses if exp["date"] == date]


def filter_by_description(expenses, description):
    return [exp for exp in expenses if description in exp["description"].lower()]


def parse_date(date):
    date = date.strip()
    if not date:
        return datetime.date.today().strftime("%Y-%m-%d"), None
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        return date, None
    except ValueError:
        return None, "Invalid format! Please use YYYY-MM-DD.\n"
