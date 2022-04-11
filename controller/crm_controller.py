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


def update_customer():
    list_customers = crm.get_list_customers()
    customer_id_to_update = input(
        "In order to update a customer, please enter an ID: ")
    if customer_id_to_update in (item for sublist in list_customers for item in sublist):
        for lst in list_customers:
            for elem in lst:
                index_of_customer_id_to_update = elem.index(customer_id_to_update)
                print(index_of_customer_id_to_update)
                print(list_customers[index_of_customer_id_to_update])
    else:
        print("Not in the list")


def delete_customer():
    view.print_error_message("Not implemented yet.")


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
