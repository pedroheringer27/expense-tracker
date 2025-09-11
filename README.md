Command-Line Expense Tracker
============================

A simple yet powerful command-line tool built with Python to help you track and manage your personal expenses. This application uses the `pandas` library to store and manipulate data, which is saved in a local `tracker.csv` file.

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

To make the tool accessible as a simple command (`expense-tracker`) from anywhere in your terminal, you need to install it as a Python package.

1.  **Save the `setup.py` file** in the same directory as `cli.py` and `expense\_tracker.py`.
    
2.  **Set up a virtual environment** (highly recommended):
    ```
      python -m venv venv
      source venv/bin/activate # On Windows, use \`venv\\Scripts\\activate\
    ```
    
3.  **Install the project in "editable" mode.** This command links the `expense-tracker` command to your source code. The `-e` flag means any changes you make to your Python files will be immediately available.
    ```
        pip install -e .
    ```
    (The `.` refers to the current directory where `setup.py` is located).
    

After installation, you can run the commands as described below from any directory.

Usage
-----

All commands are now run using the `expense-tracker` command.

### Add an Expense

**Syntax:**

```
expense-tracker add -m <amount> -d "<description>" -c "<category>"
```

**Example:**

```
expense-tracker add -m 45.50 -d "Dinner with friends" -c "Food"
```

If no category is provided, it defaults to "Misc".

### List Expenses

**List all expenses:**

```
expense-tracker list
```

**Filter by month:** (e.g., for September)

```
expense-tracker list -m 9
```

**Filter by category:**

```
expense-tracker list -c "Groceries"
```

### Summarize Expenses

**Get a summary of all expenses:**

```
expense-tracker summary
```

**Get a summary for a specific month:**

```
expense-tracker summary -m 9
```

### Delete an Expense

**Example:** (Deletes the expense with ID: 3)

```
expense-tracker delete --id 3
```

### Export Expenses

**Example:**

```
expense-tracker export my_expenses_backup
```

This will create a new file named `my_expenses_backup.csv`.

Project: https://roadmap.sh/projects/expense-tracker
