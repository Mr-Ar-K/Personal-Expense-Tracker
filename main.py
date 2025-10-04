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
        print("6. Search Expenses")
        print("7. Export Data")
        print("8. View Statistics")
        print("9. Help")
        print("10. Clear All Expenses")
        print("11. Exit")

        choice = input("Choose an option (1-11): ").strip()

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
            search_expenses_interactive(manager)
        elif choice == '7':
            export_data_interactive(manager)
        elif choice == '8':
            view_statistics_interactive(manager)
        elif choice == '9':
            help_interactive()
        elif choice == '10':
            clear_all_interactive(manager)
        elif choice == '11':
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

def help_interactive():
    print("\n--- Help ---")
    print("Personal Expense Tracker - Manage your expenses easily!")
    print("\nMenu Options:")
    print("1. Add Expense: Enter a new expense with amount, date, note, and category.")
    print("2. View Expenses: Display expenses with optional filters (category, date range).")
    print("3. Update Expense: Modify an existing expense by ID.")
    print("4. Delete Expense: Remove an expense by ID.")
    print("5. Summary Reports: View totals by category, month, or overall.")
    print("6. Search Expenses: Search expenses by note content.")
    print("7. Export Data: Export all expenses to a CSV file.")
    print("8. View Statistics: Show summary statistics (average, min, max, etc.).")
    print("9. Help: Show this help information.")
    print("10. Clear All Expenses: Delete all expenses (requires confirmation).")
    print("11. Exit: Quit the application.")
    print("\nTips:")
    print("- Dates must be in DD-MM-YYYY format (e.g., 01-10-2023).")
    print("- Amounts are in Indian Rupees (₹).")
    print("- Leave fields empty when prompted to skip optional inputs.")
    print("- All data is saved automatically to data/expenses.json.")

def clear_all_interactive(manager):
    print("\n--- Clear All Expenses ---")
    print("WARNING: This will delete ALL expenses permanently!")
    confirm = input("Type 'YES' to confirm: ").strip()
    if confirm == 'YES':
        manager.expenses = []
        manager.save_expenses()
        print("All expenses cleared.")
    else:
        print("Operation cancelled.")

def search_expenses_interactive(manager):
    print("\n--- Search Expenses ---")
    query = input("Enter search term (searches in notes): ").strip().lower()
    if not query:
        print("No search term provided.")
        return
    results = [e for e in manager.expenses if query in e['note'].lower()]
    if not results:
        print("No expenses found matching the search.")
    else:
        print(f"Found {len(results)} expense(s):")
        print_table(results)

def export_data_interactive(manager):
    print("\n--- Export Data ---")
    filename = input("Enter filename for export (e.g., expenses.csv): ").strip()
    if not filename:
        filename = "expenses_export.csv"
    if not filename.endswith('.csv'):
        filename += '.csv'
    filepath = f"data/{filename}"
    try:
        with open(filepath, 'w') as f:
            f.write("ID,Amount,Date,Note,Category\n")
            for exp in manager.expenses:
                f.write(f"{exp['id']},{exp['amount']},{exp['date']},{exp['note']},{exp['category']}\n")
        print(f"Data exported to {filepath}")
    except Exception as e:
        print(f"Error exporting data: {e}")

def view_statistics_interactive(manager):
    print("\n--- Statistics ---")
    if not manager.expenses:
        print("No expenses to analyze.")
        return
    amounts = [e['amount'] for e in manager.expenses]
    total = sum(amounts)
    count = len(amounts)
    avg = total / count
    max_exp = max(amounts)
    min_exp = min(amounts)
    print(f"Total Expenses: {count}")
    print(f"Total Amount: ₹{total:.2f}")
    print(f"Average per Expense: ₹{avg:.2f}")
    print(f"Highest Expense: ₹{max_exp:.2f}")
    print(f"Lowest Expense: ₹{min_exp:.2f}")

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