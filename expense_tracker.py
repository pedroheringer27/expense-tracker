
import pandas as pd
from pathlib import Path
import calendar

class ExpenseTracker:
    def __init__(self) -> None:
        self.file = Path("tracker.csv")
        self.data = self.load_data()

    def load_data(self):
        if self.file.exists():
            df = pd.read_csv(self.file)
        else:
            df = pd.DataFrame(columns=['Date', 'Description', 'Amount', 'Category'])
            df['Date'] = pd.to_datetime(df['Date'])
        return df

    def add_expense(self, description, amount, category=None):
        if not type(description) == str:
            raise ValueError('The description must be a string!')

        if not isinstance(amount, (int, float)):
            raise ValueError('The amount must be a number(int or float)')

        if not type(category) == str:
            raise ValueError('The description must be a string!')

        amount = int(amount*100)
        date = pd.Timestamp.now().date()
        new_row = pd.DataFrame([[date, description, amount, category]], columns=['Date', 'Description', 'Amount', 'Category'])
        data = pd.concat([self.data, new_row], ignore_index=True)
        data['Id'] = data.index + 1

        data.to_csv(self.file, index=False)
        self.data = data
        print(f"Expense added successfully (ID: {len(data)})")

    def lists(self, month=0, category='All'):
        if month == 0 and category == 'All':
            data = self.data
            data['Amount'] = data['Amount'].div(100)
            data = data[['Id','Date', 'Description',  'Amount', 'Category']]
            print(data.to_string(index=False))
        elif 0 < month <= 12 and category == 'All':
            data = self.data
            data['Amount'] = data['Amount'].div(100)
            data[['Id','Date', 'Description',  'Amount', 'Category']]
            data['Date'] = pd.to_datetime(data['Date'])
            data = data[data['Date'].dt.month == month]
            print(data.to_string(index=False))
        elif 0 < month <= 12 and category != 'All':
            data = self.data
            data['Amount'] = data['Amount'].div(100)
            data[['Id','Date', 'Description',  'Amount', 'Category']]
            data['Date'] = pd.to_datetime(data['Date'])
            data = data[data['Date'].dt.month == month and data['Category'] == category]
            print(data.to_string(index=False))
        elif month == 0 and category != 'All':
            data = self.data
            data['Amount'] = data['Amount'].div(100)
            data[['Id','Date', 'Description',  'Amount', 'Category']]
            data = data[data['Category'] == category]
            print(data.to_string(index=False))

    def summary(self, month=0, category='All'):
        if month == 0 and category == 'All':
            total_expended = self.data['Amount'].sum() 
            print(f'Total expenses: ${total_expended/100}')
        elif 0 < month <= 12 and category == 'All':
            total_expended = self.data
            total_expended['Date'] = pd.to_datetime(total_expended['Date'])
            total_expended = total_expended[total_expended['Date'].dt.month == month]['Amount'].sum()
            print(f'Total expenses for {calendar.month_name[month]}: ${total_expended/100}')
        elif 0 < month <= 12 and category != 'All':
            total_expended = self.data
            total_expended['Date'] = pd.to_datetime(total_expended['Date'])
            total_expended = total_expended[total_expended['Date'].dt.month == month and total_expended['Category'] == category]['Amount'].sum()
            print(f'Total expenses for {calendar.month_name[month]} in the category({category}): ${total_expended/100}')
        elif month == 0 and category != 'All':
            total_expended = self.data
            total_expended = total_expended[total_expended['Category'] == category]['Amount'].sum()
            print(f'Total expenses in the category({category}): ${total_expended/100}')
    def delete(self, id):
        self.data.drop([(id-1)], inplace=True)
        print("Expense deleted successfully")
        self.data.to_csv(self.file, index=False)

    def export_csv(self, file_name):
        self.data.to_csv(f'{file_name}.csv', index=False)
        print(f"Expenses exported to {file_name}.csv")

