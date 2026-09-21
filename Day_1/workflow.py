import json

print("=== RULE-BASED WORKFLOW ===")

with open("private_data.json", "r") as file:
    data = json.load(file)

question = input("User: ").lower()

if "food" in question and ("spend" in question or "spent" in question):

    total = 0

    for expense in data["expenses"]:
        if expense["category"].lower() == "food":
            total += expense["amount"]

    print("\nWorkflow:")
    print("You spent ₹" + str(total) + " on food.")

elif "travel" in question:

    total = 0

    for expense in data["expenses"]:
        if expense["category"].lower() == "travel":
            total += expense["amount"]

    print("\nWorkflow:")
    print("You spent ₹" + str(total) + " on travel.")

elif "shopping" in question:

    total = 0

    for expense in data["expenses"]:
        if expense["category"].lower() == "shopping":
            total += expense["amount"]

    print("\nWorkflow:")
    print("You spent ₹" + str(total) + " on shopping.")

elif "budget" in question:

    print("\nWorkflow:")
    print("Your monthly budget is ₹" + str(data["monthly_budget"]))

else:

    print("\nWorkflow:")
    print("Sorry, I don't have a predefined rule for this question.")