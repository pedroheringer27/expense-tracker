Command-Line Expense Tracker
============================

A simple yet powerful command-line tool built with Python to help you track and manage your personal expenses. This application uses the pandas library to store and manipulate data, which is saved in a local tracker.csv file.

Features
--------

*   **Add Expenses**: Quickly add new expenses with an amount, description, and category.
    
*   **List Transactions**: View all your expenses.
    
*   **Filter Views**: Filter the expense list by month, category, or both.
    
*   **Summarize Spending**: Get a summary of your total expenses, with the same powerful filtering options.
    
*   **Delete Entries**: Remove expenses by their unique ID.
    
*   **Export Data**: Export all your expense data to a new CSV file.
    

Installation
------------

1.  **Clone the repository or download the files** into a local directory.
    
2.  python -m venv venvsource venv/bin/activate # On Windows, use \`venv\\Scripts\\activate\`
    
3.  pip install pandas
    

Usage
-----

All commands are run from your terminal using cli.py.

### Add an Expense

To add a new expense, use the add command with the amount, description, and an optional category.

**Syntax:**


python cli.py add -m  -d "" -c ""   

**Example:**

python cli.py add -m 45.50 -d "Dinner with friends" -c "Food"

If no category is provided, it defaults to "Misc".

### List Expenses

To see a list of all your recorded expenses, use the list command.

**List all expenses:**

python cli.py list

**Filter by month:** (e.g., for September)

python cli.py list -m 9

**Filter by category:**

python cli.py list -c "Groceries"

**Filter by both month and category:**

python cli.py list -m 9 -c "Groceries"

### Summarize Expenses

To get a summary of your total spending, use the summary command. It supports the same filters as the list command.

**Get a summary of all expenses:**

python cli.py summary

**Get a summary for a specific month:** (e.g., for September)

python cli.py summary -m 9

**Get a summary for a specific category:**

python cli.py summary -c "Bills"

### Delete an Expense

To delete an expense, you first need its ID, which you can get from the list command. Then, use the delete command.

**Example:** (Deletes the expense with ID: 3)

python cli.py delete --id 3

### Export Expenses

To export all your data to a new CSV file, use the export command.

**Example:**

python cli.py export my_expenses_backup

This will create a new file named my\_expenses\_backup.csv in the same directory.
