
import argparse
from expense_tracker import ExpenseTracker

def main():
    """
    Main function to run the command-line interface for the expense tracker.
    """
    parser = argparse.ArgumentParser(
        prog="expense-tracker",
        description="A command-line tool to track and manage your personal expenses.",
        epilog="Happy tracking!"
    )

    # This creates a holder for all the different commands (add, delete, etc.)
    subparsers = parser.add_subparsers(dest='command', required=True, help="Available commands")

    # --- 'add' command ---
    add_parser = subparsers.add_parser("add", help="Add a new expense transaction.")
    add_parser.add_argument("-m", "--amount", type=float, help="The amount of the transaction (e.g., 45.50).", required=True)
    add_parser.add_argument("-d", "--description", type=str, help="A brief description of the expense.", required=True)
    add_parser.add_argument("-c", "--category", type=str, help="The category of the transaction.", default='Misc')

    # --- 'delete' command ---
    delete_parser = subparsers.add_parser("delete", help="Delete a transaction by its ID.")
    delete_parser.add_argument("--id", type=int, help="The ID of the transaction to be deleted.", required=True)

    # --- 'summary' command ---
    summary_parser = subparsers.add_parser("summary", help="Summarize total expenses with optional filters.")
    summary_parser.add_argument("-m", "--month", type=int, choices=range(1, 13), help="Filter summary by a specific month (1-12).", default=0)
    summary_parser.add_argument("-c", "--category", type=str, help="Filter summary by a specific category.", default='All')

    # --- 'list' command ---
    list_parser = subparsers.add_parser("list", help="List all transactions with optional filters.")
    list_parser.add_argument("-m", "--month", type=int, choices=range(1, 13), help="Filter list by a specific month (1-12).", default=0)
    list_parser.add_argument("-c", "--category", type=str, help="Filter list by a specific category.", default='All')

    # --- 'export' command ---
    export_parser = subparsers.add_parser("export", help="Export all expenses to a new CSV file.")
    export_parser.add_argument("filename", type=str, help="The name of the new CSV file (e.g., 'my_expenses_export').")

    args = parser.parse_args()
    tracker = ExpenseTracker()

    # for handling mutually exclusive commands.
    if args.command == 'add':
        tracker.add_expense(args.description, args.amount, args.category)
    elif args.command == 'delete':
        tracker.delete(args.id)
    elif args.command == 'summary':
        tracker.summary(args.month, args.category)
    elif args.command == 'list':
        tracker.list_expenses(args.month, args.category)
    elif args.command == 'export':
        tracker.export_csv(args.filename)

if __name__ == "__main__":
    main()

