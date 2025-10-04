# Personal-Expense-Tracker

#### Menu Options

1. **Add Expense**: Enter a new expense with amount, date (DD-MM-YYYY), note, and category
2. **View Expenses**: View all expenses with optional filters (category, date range)
3. **Update Expense**: Modify an existing expense by ID
4. **Delete Expense**: Remove an expense by ID
5. **Summary Reports**: View spending summaries (total, by category, by month)
6. **Search Expenses**: Search expenses by note content
7. **Export Data**: Export all expenses to a CSV file
8. **View Statistics**: Show summary statistics (average, min, max, etc.)
9. **Help**: Display help information and tips
10. **Clear All Expenses**: Delete all expenses (with confirmation)
11. **Exit**: Quit the applicationOptions

1. **Add Expense**: Enter a new expense with amount, date (DD-MM-YYYY), note, and category
2. **View Expenses**: Display expenses with optional filters
3. **Update Expense**: Modify an existing expense by ID
4. **Delete Expense**: Remove an expense by ID
5. **Summary Reports**: View spending summaries (total, by category, by month)
6. **Help**: Show detailed help and usage information
7. **Clear All Expenses**: Delete all expenses (with confirmation)
8. **Exit**: Quit the application
A simple, user-friendly Personal Expense Tracker built in Python using standard libraries.

## Features

- Interactive menu-driven interface
- Add, view, update, delete expenses
- Categories and notes
- Summary reports: total, by category, by month
- Filters by category or date range
- Data stored in JSON file

## Usage

Run `python main.py` to start the interactive menu.

The application will guide you through each operation with prompts.

### Menu Options

1. **Add Expense**: Enter amount, date (DD-MM-YYYY), note, and category
2. **View Expenses**: View all expenses with optional filters
3. **Update Expense**: Modify existing expenses by ID
4. **Delete Expense**: Remove expenses by ID
5. **Summary Reports**: View spending summaries
6. **Exit**: Quit the application

### Example Session

```
Welcome to Personal Expense Tracker!
========================================

Menu:
1. Add Expense
2. View Expenses
3. Update Expense
4. Delete Expense
5. Summary Reports
6. Exit
Choose an option (1-6): 1

--- Add New Expense ---
Enter amount (₹): 10.50
Enter date (DD-MM-YYYY): 01-10-2023
Enter note: Lunch
Enter category: Food
Expense added successfully with ID: 1
```