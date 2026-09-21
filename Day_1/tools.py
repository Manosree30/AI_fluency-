import json


def read_expenses():
    """Read the private expense data."""

    with open("private_data.json", "r") as file:
        data = json.load(file)

    return data


def calculate_category_total(category):
    """Calculate total spending for a category."""

    data = read_expenses()

    total = 0

    for expense in data["expenses"]:
        if expense["category"].lower() == category.lower():
            total += expense["amount"]

    return total


def get_budget():
    """Get the monthly budget."""

    data = read_expenses()

    return data["monthly_budget"]