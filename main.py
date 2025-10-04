import argparse
from expense_manager import ExpenseManager

def main():
    manager = ExpenseManager()

    print("Welcome to Personal Expense Tracker!")
    print("=" * 40)

    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Summary Reports")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == '1':
            add_expense_interactive(manager)
        elif choice == '2':
            view_expenses_interactive(manager)
        elif choice == '3':
            update_expense_interactive(manager)
        elif choice == '4':
            delete_expense_interactive(manager)
        elif choice == '5':
            summary_interactive(manager)
        elif choice == '6':
            print("Thank you for using Personal Expense Tracker!")
            break
        else:
            print("Invalid choice. Please try again.")

def add_expense_interactive(manager):
    print("\n--- Add New Expense ---")
    while True:
        amount = input("Enter amount (₹): ").strip()
        try:
            amount = float(amount)
            if amount <= 0:
                print("Amount must be positive.")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")

    while True:
        date = input("Enter date (DD-MM-YYYY): ").strip()
        try:
            from datetime import datetime
            datetime.strptime(date, '%d-%m-%Y')
            break
        except ValueError:
            print("Invalid date format. Use DD-MM-YYYY.")

    note = input("Enter note: ").strip()
    category = input("Enter category: ").strip()

    try:
        id = manager.add_expense(amount, date, note, category)
        print(f"Expense added successfully with ID: {id}")
    except ValueError as e:
        print(f"Error: {e}")

def view_expenses_interactive(manager):
    print("\n--- View Expenses ---")
    category = input("Filter by category (leave empty for all): ").strip()
    if category == '':
        category = None
    date_from = input("Filter from date (DD-MM-YYYY, leave empty for no filter): ").strip()
    if date_from == '':
        date_from = None
    else:
        try:
            from datetime import datetime
            datetime.strptime(date_from, '%d-%m-%Y')
        except ValueError:
            print("Invalid date format. Ignoring date filter.")
            date_from = None
    date_to = input("Filter to date (DD-MM-YYYY, leave empty for no filter): ").strip()
    if date_to == '':
        date_to = None
    else:
        try:
            from datetime import datetime
            datetime.strptime(date_to, '%d-%m-%Y')
        except ValueError:
            print("Invalid date format. Ignoring date filter.")
            date_to = None

    expenses = manager.view_expenses(category, date_from, date_to)
    if not expenses:
        print("No expenses found.")
    else:
        print_table(expenses)

def update_expense_interactive(manager):
    print("\n--- Update Expense ---")
    while True:
        id_str = input("Enter expense ID to update: ").strip()
        try:
            id = int(id_str)
            break
        except ValueError:
            print("Invalid ID. Please enter a number.")

    print("Leave fields empty to keep current values.")
    amount = input("New amount (₹): ").strip() or None
    date = input("New date (DD-MM-YYYY): ").strip() or None
    note = input("New note: ").strip() or None
    category = input("New category: ").strip() or None

    try:
        if manager.update_expense(id, amount, date, note, category):
            print("Expense updated successfully.")
        else:
            print("Expense not found.")
    except ValueError as e:
        print(f"Error: {e}")

def delete_expense_interactive(manager):
    print("\n--- Delete Expense ---")
    while True:
        id_str = input("Enter expense ID to delete: ").strip()
        try:
            id = int(id_str)
            break
        except ValueError:
            print("Invalid ID. Please enter a number.")

    if manager.delete_expense(id):
        print("Expense deleted successfully.")
    else:
        print("Expense not found.")

def summary_interactive(manager):
    print("\n--- Summary Reports ---")
    print("1. Total Spent")
    print("2. By Category")
    print("3. By Month")

    sub_choice = input("Choose summary type (1-3): ").strip()

    if sub_choice == '1':
        total = manager.summary_total()
        print(f"Total spent: ₹{total:.2f}")
    elif sub_choice == '2':
        summary = manager.summary_by_category()
        if not summary:
            print("No expenses.")
        else:
            for cat, amt in summary.items():
                print(f"{cat}: ₹{amt:.2f}")
    elif sub_choice == '3':
        summary = manager.summary_by_month()
        if not summary:
            print("No expenses.")
        else:
            for mon, amt in summary.items():
                print(f"{mon}: ₹{amt:.2f}")
    else:
        print("Invalid choice.")

def print_table(expenses):
    if not expenses:
        return
    # Headers
    print(f"{'ID':<5} {'Amount':<10} {'Date':<12} {'Category':<15} {'Note'}")
    print("-" * 60)
    for exp in expenses:
        print(f"{exp['id']:<5} ₹{exp['amount']:<9.2f} {exp['date']:<12} {exp['category']:<15} {exp['note']}")

if __name__ == '__main__':
    main()