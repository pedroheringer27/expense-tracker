
import pandas as pd
from pathlib import Path
import calendar
import os

class ExpenseTracker:
    """
    A class to manage and track expenses using a CSV file.
    
    This class handles loading, adding, deleting, filtering, and summarizing
    expense data stored in a pandas DataFrame and persisted to a CSV file.
    """

    def __init__(self, file_path:str = "tracker.csv") -> None:
        """
        Initializes the ExpenseTracker.

        Args:
            file_path (str): The path to the CSV file where expenses are stored.
        """

        self.file = Path("tracker.csv")
        self.columns = ['Id', 'Date', 'Description', 'Amount', 'Category']
        self.data = self.load_data()

    def load_data(self) -> pd.DataFrame:
        """
        Loads expense data from the CSV file.
        
        If the file doesn't exist or is empty, it creates a new DataFrame
        with the correct columns and saves the file.
        """

        if not self.file.exists() or os.path.getsize(self.file) == 0:
            df = pd.DataFrame(columns=self.columns)
            df.to_csv(self.file, index=False)
        df = pd.read_csv(self.file)
        df['Date'] = pd.to_datetime(df['Date'])
        return df


    def add_expense(self, description, amount, category="Misc"):
        """
        Adds a new expense to the tracker.

        Args:
            description (str): A description of the expense.
            amount (float or int): The monetary value of the expense.
            category (str, optional): The category of the expense. Defaults to None.

        Raises:
            ValueError: If the input types for description, amount, or category are invalid.
        """

        if not isinstance(description, str) or not description:
            raise ValueError('The description must be a non-empty string!')
       

        if not isinstance(amount, (int, float)):
            raise ValueError('The amount must be a number(int or float)')

        if not isinstance(category, str):
            raise ValueError('The category must be a string!')

        amount = int(amount*100)
        date = pd.Timestamp.now().date()

        new_row = pd.DataFrame([{
            'Date': date, 
            'Description': description, 
            'Amount': amount, 
            'Category': category
        }])
        new_row['Date'] = pd.to_datetime(new_row['Date'])
        self.data = pd.concat([self.data, new_row], ignore_index=True)
        self.data['Id'] = self.data.index + 1

        self.data.to_csv(self.file, index=False)
        print(f"Expense added successfully (ID: {len(self.data)})")

    def _filter_data(self, month: int = 0, category: str = 'All') -> pd.DataFrame:
        """
        A private helper method to filter the expense data.
        
        Args:
            month (int): The month number (1-12) to filter by. 0 means all months.
            category (str): The category to filter by. 'All' means all categories.

        Returns:
            pd.DataFrame: A new DataFrame containing the filtered data.
        """
        filtered_df = self.data.copy()

        if month in range(1, 13):
            filtered_df = filtered_df[filtered_df['Date'].dt.month == month]

        if category != 'All':
            filtered_df = filtered_df.loc[filtered_df['Category'].astype(str).str.lower() == category.lower()]

        filtered_df = pd.DataFrame(filtered_df)
        return filtered_df

    def list_expenses(self, month: int = 0, category: str = 'All') -> None:
        """
        Lists and prints expenses based on filters.
        """
        
        expenses = self._filter_data(month, category)

        if expenses.empty:
            print("No expenses found matching the criteria.")
            return

        display_df = expenses.copy()
        display_df['Amount'] = display_df['Amount'] / 100

        print(display_df.to_string(index=False))

    def summary(self, month: int = 0, category: str = 'All') -> None:
        """
        Calculates and prints a summary of total expenses based on optional filters.
        """

        expenses = self._filter_data(month, category)

        if expenses.empty:
            print("No expenses found matching the criteria.")
            return
        
        total_expended = expenses.copy()
        total_expended = total_expended['Amount'].sum() / 100

        month_name = f" for {calendar.month_name[month]}" if month in range(1, 13) else ""
        category_name = f" in the '{category}' category" if category != 'All' else ""
        
        print(f"Total expenses{month_name}{category_name}: ${total_expended:.2f}")

    def delete(self, id: int) -> None:
        """
        Deletes an expense using its ID.

        Args:
            id (int): The ID of the expense to be deleted.
        """
        if id not in self.data['Id'].values:
            print(f"ERROR: Expense with ID {id} not found.")
            return

        self.data.drop([(id-1)], inplace=True)
        self.data.to_csv(self.file, index=False)
        print("Expense deleted successfully")

    def export_csv(self, file_name):
        """
        Exports the current expenses to a new CSV file.

        Args:
            file_name (str): The desired name for the exported file (without extension).
        """
        self.data.to_csv(f'{file_name}.csv', index=False)
        print(f"Expenses exported to {file_name}.csv")

