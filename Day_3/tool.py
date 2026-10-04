def calculate_expense(amount, quantity):
    """
    Calculate the total expense.

    Parameters:
        amount: Price of one item
        quantity: Number of items

    Returns:
        Total expense as text
    """

    try:
        amount = float(amount)
        quantity = int(quantity)

        if amount < 0 or quantity < 0:
            return "Error: Amount and quantity cannot be negative."

        total = amount * quantity

        return f"Total expense = ₹{total:.2f}"

    except (ValueError, TypeError):
        return "Error: Please provide a valid amount and quantity."