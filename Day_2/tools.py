def get_workshop_details(workshop_name):

    workshops = {
        "AI Engineering": {
            "fee": 2500,
            "duration": "3 days",
            "placement_score": 9
        },

        "Full Stack Development": {
            "fee": 1800,
            "duration": "2 days",
            "placement_score": 8
        },

        "Data Analytics": {
            "fee": 2200,
            "duration": "3 days",
            "placement_score": 7
        }
    }

    return workshops.get(
        workshop_name,
        "Workshop not found"
    )


def calculator(expression):

    try:
        allowed = "0123456789+-*/(). "

        if not all(char in allowed for char in expression):
            return "Invalid expression"

        return eval(expression, {"__builtins__": None}, {})

    except Exception as e:

        return f"Calculation error: {e}"