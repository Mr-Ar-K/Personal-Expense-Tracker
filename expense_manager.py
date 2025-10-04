import json
import os
from datetime import datetime
from collections import defaultdict

class ExpenseManager:
    def __init__(self, data_file='data/expenses.json'):
        self.data_file = data_file
        self.expenses = self.load_expenses()

    def load_expenses(self):
        if os.path.exists(self.data_file):
            expenses = json.load(open(self.data_file, 'r'))
            # Convert old date format if necessary
            for exp in expenses:
                if len(exp['date']) == 8 and '-' not in exp['date']:
                    dt = datetime.strptime(exp['date'], '%d%m%Y')
                    exp['date'] = dt.strftime('%d-%m-%Y')
            with open(self.data_file, 'w') as f:
                json.dump(expenses, f, indent=4)
            return expenses
        return []

    def save_expenses(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.expenses, f, indent=4)

    def add_expense(self, amount, date, note, category):
        # Validate amount
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Amount must be positive")
        except ValueError:
            raise ValueError("Invalid amount")

        # Validate date
        try:
            datetime.strptime(date, '%d-%m-%Y')
        except ValueError:
            raise ValueError("Invalid date format. Use DD-MM-YYYY")

        # Auto generate id
        ids = [exp['id'] for exp in self.expenses]
        new_id = max(ids) + 1 if ids else 1

        expense = {
            'id': new_id,
            'amount': amount,
            'date': date,
            'note': note,
            'category': category
        }
        self.expenses.append(expense)
        self.save_expenses()
        return new_id

    def view_expenses(self, category=None, date_from=None, date_to=None):
        filtered = self.expenses
        if category:
            filtered = [e for e in filtered if e['category'].lower() == category.lower()]
        if date_from:
            date_from_dt = datetime.strptime(date_from, '%d-%m-%Y')
            filtered = [e for e in filtered if datetime.strptime(e['date'], '%d-%m-%Y') >= date_from_dt]
        if date_to:
            date_to_dt = datetime.strptime(date_to, '%d-%m-%Y')
            filtered = [e for e in filtered if datetime.strptime(e['date'], '%d-%m-%Y') <= date_to_dt]
        return filtered

    def update_expense(self, id, amount=None, date=None, note=None, category=None):
        for exp in self.expenses:
            if exp['id'] == id:
                if amount is not None:
                    try:
                        amount = float(amount)
                        if amount <= 0:
                            raise ValueError("Amount must be positive")
                        exp['amount'] = amount
                    except ValueError:
                        raise ValueError("Invalid amount")
                if date is not None:
                    try:
                        datetime.strptime(date, '%d-%m-%Y')
                        exp['date'] = date
                    except ValueError:
                        raise ValueError("Invalid date format. Use DD-MM-YYYY")
                if note is not None:
                    exp['note'] = note
                if category is not None:
                    exp['category'] = category
                self.save_expenses()
                return True
        return False

    def delete_expense(self, id):
        for i, exp in enumerate(self.expenses):
            if exp['id'] == id:
                del self.expenses[i]
                self.save_expenses()
                return True
        return False

    def summary_total(self):
        return sum(e['amount'] for e in self.expenses)

    def summary_by_category(self):
        summary = defaultdict(float)
        for e in self.expenses:
            summary[e['category']] += e['amount']
        return dict(summary)

    def summary_by_month(self):
        summary = defaultdict(float)
        for e in self.expenses:
            dt = datetime.strptime(e['date'], '%d-%m-%Y')
            month = dt.strftime('%m-%Y')  # MM-YYYY
            summary[month] += e['amount']
        return dict(summary)