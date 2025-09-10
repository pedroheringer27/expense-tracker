
import argparse

parser = argparse.ArgumentParser(prog="expense-tracker", description="Stores and show expenses.", epilog="That's it guys.")
subparser = parser.add_subparsers(help="subcommand help")

add = subparser.add_parser("add", help="Add's a new expense transaction.")
add.add_argument("-desc", "--description", type=str, help="Add the description of the transaction.")
add.add_argument("-amnt", "--amount", type=float, help="Add the amount of the transaction.")

delete = subparser.add_parser("delete", help="Delete a transaction using it's id.")
delete.add_argument("--id", type=int, help="The id of the transaction to be deleted.")

summary = subparser.add_parser("summary", help="Sumarizes the expenses based on the filter.")
summary.add_argument("-m", "--month", type=int, help="The month to summarize the transactions.")

show = subparser.add_parser("list", help="List's all transactions.")

args = parser.parse_args()

print(args.description)
print(args.amount)
