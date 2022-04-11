from model.crm import crm
from view import terminal as view
from model import data_manager, util



def list_customers():
    list_customers = crm.get_list_customers()
    view.print_table(list_customers)


def add_customer():
    list_customers = crm.get_list_customers()
    new_customer = view.get_inputs()
    list_customers.append(new_customer)
    data_manager.write_table_to_file(
        crm.DATAFILE, list_customers, separator=';')

def get_client_from_id(list_customers,customer_id_to_update):
    for item, sublist in enumerate(list_customers):
        try:
            return (item,sublist.index(customer_id_to_update))
        except ValueError:
            continue
    return None

def update_customer():
    list_customers = crm.get_list_customers()
    customer_id_to_update = input(
        "In order to update a customer, please enter an ID: ")
    customer_index = get_client_from_id(list_customers,customer_id_to_update )
    if customer_index is not None:
        client_update_name = str(input("update name : "))
        client_update_mail = str(input("update mail"))
        client_update_subs = str(input("update subs"))
        client_update = [customer_id_to_update, client_update_name,client_update_mail,client_update_subs]
        list_customers[customer_index[0]] = client_update
        data_manager.write_table_to_file(
        crm.DATAFILE, list_customers, separator=';')
    else :
        print("nu este in lista")



def delete_customer():
    list_customers = crm.get_list_customers()
    customer_id_to_update = input(
        "In order to update a customer, please enter an ID: ")
    customer_index = get_client_from_id(list_customers,customer_id_to_update )
    if customer_index is not None:
        list_customers.pop(customer_index[0])
        data_manager.write_table_to_file(
        crm.DATAFILE, list_customers, separator=';')
    else :
        print("nu este in lista")


def get_subscribed_emails():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
