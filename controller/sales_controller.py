from model.sales import sales
from view import terminal as view
from model import data_manager, util
from controller import main_controller
from tabulate import tabulate
import TableIt
from datetime import date, datetime, timedelta


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


def get_biggest_revenue():
    '''Get the the biggest revenue'''
    transactions = sales.get_transactions()
    revenues = []
    for transaction in transactions:
        revenue = transaction[-2]
        revenues.append(revenue)
    revenues_float = [float(revenue) for revenue in revenues]
    biggest_revenue = max(revenues_float)
    return biggest_revenue


def get_biggest_revenue_transaction_simple_list():
    '''Get the transaction that made the biggest revenue as a single list'''
    transactions = sales.get_transactions()
    biggest_revenue = get_biggest_revenue()
    for transaction in transactions:
        for item in transaction:
            if item == str(biggest_revenue):
                index_transaction = transactions.index(transaction)
    biggest_revenue_single_transaction = transactions[index_transaction]
    return biggest_revenue_single_transaction


def get_biggest_revenue_transaction():
    '''Get the transaction that made the biggest revenue as table'''
    transactions = sales.get_transactions()
    print("BIGGEST REVENUE TRANSACTION")
    biggest_revenue = get_biggest_revenue()
    for transaction in transactions:
        for item in transaction:
            if item == str(biggest_revenue):
                index_transaction = transactions.index(transaction)
    biggest_revenue_single_transaction = transactions[index_transaction]
    TableIt.printTable([biggest_revenue_single_transaction, ])
    return biggest_revenue_single_transaction


def get_biggest_revenue_product_name():
    '''Get the name of the product that made the biggest revenue in one transaction'''
    biggest_revenue_single_transaction = get_biggest_revenue_transaction_simple_list()
    product_name_biggest_revenue_transaction = biggest_revenue_single_transaction[2]
    return product_name_biggest_revenue_transaction

  
def get_biggest_revenue_product():
    transactions = sales.get_transactions()
    products = []
    for transaction in transactions:
        products.append(transaction[2])
    #check for duplicates
    unique_products = set(products)
    if len(products) == len(unique_products):
        print(
            f'The product that made the biggest revenue altogether is: {get_biggest_revenue_product_name()}')
    else:
        filter_products = []
        multiple_products = []
        for product in products:
            if product not in filter_products:
                filter_products.append(product)
            else:
                multiple_products.append(product)
        products_with_duplicates = list(set(multiple_products))

        transaction_multiple_products0 = []
        transaction_multiple_products1 = []
        transaction_multiple_products2 = []
        transaction_multiple_products3 = []
        transaction_multiple_products4 = []

        for transaction in transactions:
            for i in range(len(products_with_duplicates)):
                if products_with_duplicates[i] == transaction[2] and i == 0:
                    transaction_multiple_products0.append(transaction)
                elif products_with_duplicates[i] == transaction[2] and i == 1:
                    transaction_multiple_products1.append(transaction)
                elif products_with_duplicates[i] == transaction[2] and i == 2:
                    transaction_multiple_products2.append(transaction)
                elif products_with_duplicates[i] == transaction[2] and i == 3:
                    transaction_multiple_products3.append(transaction)
                elif products_with_duplicates[i] == transaction[2] and i == 4:
                    transaction_multiple_products4.append(transaction)
        sum0 = 0
        for transaction in transaction_multiple_products0:
            price = transaction[-2]
            sum0 += float(price)
        sum1 = 0
        for transaction in transaction_multiple_products1:
            price = transaction[-2]
            sum1 += float(price)
        sum2 = 0
        for transaction in transaction_multiple_products2:
            price = transaction[-2]
            sum2 += float(price)
        sum3 = 0
        for transaction in transaction_multiple_products3:
            price = transaction[-2]
            sum3 += float(price)
        sum4 = 0
        for transaction in transaction_multiple_products4:
            price = transaction[-2]
            sum4 += float(price)
        sum_max = max(sum0, sum1, sum2, sum3, sum4)
        
        if sum_max == sum0:
            print(
                f'The product that made the biggest revenue altogether is: {transaction_multiple_products0[0][2]}')
        elif sum_max == sum1:
            print(
                f'The product that made the biggest revenue altogether is: {transaction_multiple_products1[0][2]}')
        elif sum_max == sum2:
            print(
                f'The product that made the biggest revenue altogether is: {transaction_multiple_products2[0][2]}')
        elif sum_max == sum3:
            print(
                f'The product that made the biggest revenue altogether is: {transaction_multiple_products3[0][2]}')
        elif sum_max == sum4:
            print(
                f'The product that made the biggest revenue altogether is: {transaction_multiple_products4[0][2]}')


def count_transactions_between():
    transactions_list = sales.get_transactions()
    date_index = 4
    first_search_date = input("Enter first date in yyyy-mm-dd format: ")
    second_search_date = input("Enter the second date in  yyyy-mm-dd format: ")
    first_search_date = datetime.strptime(first_search_date, "%Y-%m-%d").date() 
    second_search_date = datetime.strptime(second_search_date, "%Y-%m-%d").date()
    
    filtered_by_date_transactions = []
    for transaction in transactions_list:
        date_of_transaction = datetime.strptime(
            transaction[date_index], "%Y-%m-%d").date()
        if (date_of_transaction >= first_search_date) and (date_of_transaction <= second_search_date):
            filtered_by_date_transactions.append(transaction)
    if len(filtered_by_date_transactions) > 0:
        view.print_message(
            f'The number of transactions between {first_search_date} and {second_search_date} is: {len(filtered_by_date_transactions)}')
        return filtered_by_date_transactions
    else:
        return "No transactions were made in this time span!"



def sum_transactions_between():
    # filtered_by_date_transactions = 


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
        main_controller.menu()
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
