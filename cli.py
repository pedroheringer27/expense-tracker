
import argparse
from expense_tracker import ExpenseTracker

parser = argparse.ArgumentParser(prog="expense-tracker", description="Stores and show expenses.", epilog="That's it guys.")
subparser = parser.add_subparsers(dest='command', required=True)

add = subparser.add_parser("add", help="Add's a new expense transaction.")
add.add_argument("-desc", "--description", type=str, help="Add the description of the transaction.", required=True)
add.add_argument("-amnt", "--amount", type=float, help="Add the amount of the transaction.", required=True)
add.add_argument("--category", type=str, help="Add the category of the transaction.", default='Misc')


delete = subparser.add_parser("delete", help="Delete a transaction using it's id.")
delete.add_argument("--id", type=int, help="The id of the transaction to be deleted.", required=True)

summary = subparser.add_parser("summary", help="Sumarizes the expenses based on the filter.")
summary.add_argument("-m", "--month", type=int, choices=range(1,12), help="The month to summarize the transactions.", default=0)
summary.add_argument("--category", type=str, help="Filter summary by category.", default='All')

show = subparser.add_parser("list", help="List's all transactions.")
show.add_argument('-m', '--month', choices=range(1,12), help='The month of the transactions to show.', default=0)
show.add_argument("--category", type=str, help="Filter summary by category.", default='All')

export = subparser.add_parser("export", help='Exports the expenses to a .csv file')
export.add_argument('-f', '--file', type=str, required=True, help="Name of the .csv file")

args = parser.parse_args()

tracker = ExpenseTracker()

if args.command == 'add':
    tracker.add_expense(args.description, args.amount, args.category)

if args.command == 'delete':
    tracker.delete(args.id)

if args.command == 'summary':
    tracker.summary(args.month, args.category)

if args.command == 'show':
    tracker.lists(args.month, args.category)

if args.command == 'export':
    tracker.export_csv(args.file)

