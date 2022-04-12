from model.sales import sales
from view import terminal as view
from model import data_manager, util


def list_transactions():
    transactions = sales.get_transactions()
    view.print_table_sales(transactions)


def add_transaction():
    transactions = sales.get_transactions()
    new_transaction = view.get_inputs_sales()
    transactions.append(new_transaction)
    data_manager.write_table_to_file(
        sales.DATAFILE, transactions, separator=';')


def get_transaction_from_id(transactions, transaction_id_to_update):
    for item, sublist in enumerate(transactions):
        try:
            return (item, sublist.index(transaction_id_to_update))
        except ValueError:
            continue
    return None


def update_transaction():
    transactions = sales.get_transactions()
    transaction_id_to_update = input(
        "In order to update a transaction, please enter an ID: ")
    transaction_tuple = get_transaction_from_id(
        transactions, transaction_id_to_update)
    transaction_index = transaction_tuple[0]
    if transaction_tuple is not None:
        transaction_update_name = str(input("Update the customer name: "))
        transaction_update_product = str(input("Update the product: "))
        transaction_update_price = str(input("Update the price: "))
        transaction_update_date = str(input("Update the date: "))
        transaction_update = [transaction_id_to_update, transaction_update_name,\
                              transaction_update_product, transaction_update_price,\
                              transaction_update_date]
        transactions[transaction_index] = transaction_update
        data_manager.write_table_to_file(
            sales.DATAFILE, transactions, separator=';')
    else:
        print("Not an ID in the list of transactions")


def delete_transaction():
    transactions = sales.get_transactions()
    transaction_id_to_delete = input(
        "In order to delete a transaction, please enter an ID: ")
    transaction_tuple = get_transaction_from_id(
        transactions, transaction_id_to_delete)
    transaction_index = transaction_tuple[0]
    if transactions is not None:
        transactions.pop(transaction_index)
        data_manager.write_table_to_file(
            sales.DATAFILE, transactions, separator=';')
    else:
        print("Not an ID in the list of customers")


def get_biggest_revenue_transaction():
    view.print_error_message("Not implemented yet.")


def get_biggest_revenue_product():
    view.print_error_message("Not implemented yet.")


def count_transactions_between():
    view.print_error_message("Not implemented yet.")


def sum_transactions_between():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum the price of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
