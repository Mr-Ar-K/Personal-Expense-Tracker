# Personal Expense Tracker

A simple, interactive command-line Personal Expense Tracker built in Python. Easily manage your daily expenses with categories, notes, and powerful filtering and reporting features.

## Features

- **Interactive Menu Interface**: User-friendly menu-driven navigation
- **Expense Management**: Add, view, update, and delete expenses
- **Advanced Filtering**: Filter expenses by category and date range
- **Search Functionality**: Search expenses by note content
- **Summary Reports**: View totals by category, month, or overall spending
- **Data Export**: Export expenses to CSV format
- **Statistics**: Quick insights with averages, min/max values
- **Data Persistence**: Automatic saving to JSON file
- **Input Validation**: Robust validation for amounts and dates
- **Indian Rupee Support**: Currency display in ₹

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library modules)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Mr-Ar-K/Personal-Expense-Tracker.git
   cd Personal-Expense-Tracker
   ```

2. Run the application:
   ```bash
   python main.py
   ```

## Usage

The application starts with a welcome screen and presents an interactive menu. Simply choose options by entering the corresponding number.

### Menu Options

1. **Add Expense**: Enter a new expense with amount (₹), date (DD-MM-YYYY), note, and category
2. **View Expenses**: Display all expenses with optional filters (category, date range)
3. **Update Expense**: Modify existing expenses by ID (selective field updates)
4. **Delete Expense**: Remove expenses by ID
5. **Summary Reports**: View spending summaries (total, by category, by month)
6. **Search Expenses**: Find expenses by searching note content
7. **Export Data**: Export all expenses to a CSV file
8. **View Statistics**: Display summary statistics (count, total, average, min/max)
9. **Help**: Show detailed help information and usage tips
10. **Clear All Expenses**: Delete all expenses (with confirmation)
11. **Exit**: Quit the application

## Examples

### Adding an Expense
```
--- Add New Expense ---
Enter amount (₹): 250.50
Enter date (DD-MM-YYYY): 15-10-2023
Enter note: Grocery shopping
Enter category: Food
Expense added successfully with ID: 1
```

### Viewing Expenses
```
--- View Expenses ---
Filter by category (leave empty for all): Food
Filter from date (DD-MM-YYYY, leave empty for no filter): 01-10-2023
Filter to date (DD-MM-YYYY, leave empty for no filter): 31-10-2023

ID    Amount     Date         Category        Note
------------------------------------------------------------
1     ₹250.50    15-10-2023   Food            Grocery shopping
```

### Summary Reports
```
--- Summary Reports ---
1. Total Spent
2. By Category
3. By Month
Choose summary type (1-3): 2

Food: ₹250.50
Transport: ₹150.00
```

## Data Storage

- All expense data is automatically saved to `data/expenses.json`
- Data persists between sessions
- JSON format allows for easy backup and portability
- Exported CSV files are saved in the `data/` directory

## Tips

- **Date Format**: Always use DD-MM-YYYY format (e.g., 01-10-2023 for 1st October 2023)
- **Currency**: All amounts are displayed in Indian Rupees (₹)
- **Optional Fields**: Leave prompts empty to skip optional inputs
- **Search**: Use keywords in notes for flexible searching
- **Export**: CSV files can be opened in Excel or other spreadsheet applications
- **Backup**: Regularly export data or copy `data/expenses.json` for backup

## File Structure

```
Personal-Expense-Tracker/
├── main.py                 # Main application entry point
├── expense_manager.py      # Core expense management logic
├── requirements.txt        # Dependencies (none required)
├── README.md              # This file
└── data/
    └── expenses.json      # Expense data storage
```
