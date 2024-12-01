import json

BUDGET_FILE = "budget_data.json"

# Load data from the budget file or initialize if it doesn't exist
def load_data():
    try:
        with open(BUDGET_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"income": 0, "expenses": [], "budgets": {}}

# Save the data to the budget file
def save_data(data):
    with open(BUDGET_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Add income
def add_income(data):
    income = float(input("Enter your income: "))
    data["income"] = income
    save_data(data)
    print(f"Income of {income} added successfully.")

# Add an expense
def add_expense(data):
    category = input("Enter expense category (e.g., food, rent): ").strip()
    amount = float(input("Enter expense amount: "))
    data["expenses"].append({"category": category, "amount": amount})
    save_data(data)
    print(f"Expense of {amount} in {category} added successfully.")

# Set a budget for a category
def set_budget(data):
    category = input("Enter category to set a budget for (e.g., food, rent): ").strip()
    budget_amount = float(input(f"Enter budget for {category}: "))
    data["budgets"][category] = budget_amount
    save_data(data)
    print(f"Budget of {budget_amount} set for {category}.")

# View financial summary
def view_summary(data):
    total_expenses = sum(expense["amount"] for expense in data["expenses"])
    print("\n--- Financial Summary ---")
    print(f"Total Income: {data['income']}")
    print(f"Total Expenses: {total_expenses}")
    print(f"Remaining Income: {data['income'] - total_expenses}")
    
    print("\n--- Budget Overview ---")
    for category, budget in data["budgets"].items():
        spent = sum(expense["amount"] for expense in data["expenses"] if expense["category"] == category)
        remaining = budget - spent
        print(f"{category}: Budgeted: {budget}, Spent: {spent}, Remaining: {remaining}")

# Main program loop
def main():
    data = load_data()
    
    print("Welcome to BudgetBuddy!")
    
    while True:
        print("\nMenu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Set Budget")
        print("4. View Financial Summary")
        print("5. Exit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            add_income(data)
        elif choice == "2":
            add_expense(data)
        elif choice == "3":
            set_budget(data)
        elif choice == "4":
            view_summary(data)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
