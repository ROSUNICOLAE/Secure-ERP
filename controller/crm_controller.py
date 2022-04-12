from model.crm import crm
from view import terminal as view
from model import data_manager, util
from controller import main_controller



def list_customers():
    list_customers = crm.get_list_customers()
    view.print_table(list_customers)


def add_customer():
    list_customers = crm.get_list_customers()
    new_customer = view.get_inputs()
    list_customers.append(new_customer)
    data_manager.write_table_to_file(
        crm.DATAFILE, list_customers, separator=';')
    
    
def get_client_from_id(list_customers, customer_id_to_update):
    for item, sublist in enumerate(list_customers):
        try:
            return (item, sublist.index(customer_id_to_update))
        except ValueError:
            continue
    return None


def update_customer():
    list_customers = crm.get_list_customers()
    customer_id_to_update = input(
        "In order to update a customer, please enter an ID: ")
    customer_tuple = get_client_from_id(list_customers, customer_id_to_update)
    customer_index = customer_tuple[0]
    if customer_tuple is not None:
        client_update_name = str(input("Update name: "))
        client_update_mail = str(input("Update mail: "))
        client_update_subscription = str(input("Update subscription: "))
        client_update = [customer_id_to_update, client_update_name, client_update_mail, client_update_subscription]
        list_customers[customer_index] = client_update
        data_manager.write_table_to_file(crm.DATAFILE, list_customers, separator=';')
    else:
        print("Not an ID in the list of customers")



def delete_customer():
    list_customers = crm.get_list_customers()
    customer_id_to_update = input(
        "In order to delete a customer, please enter an ID: ")
    customer_tuple = get_client_from_id(list_customers, customer_id_to_update)
    customer_index = customer_tuple[0]
    if customer_tuple is not None:
        list_customers.pop(customer_index)
        data_manager.write_table_to_file(crm.DATAFILE, list_customers, separator=';')
    else:
        print("Not an ID in the list of customers")


def get_subscribed_emails():
    '''Get the emails of subscribed customers'''
    list_customers = crm.get_list_customers()
    list_of_emails = []
    print("Email adresses of the subscribed customers:")
    for customer_information in list_customers:
        customer_mail = customer_information[2]
        subscription = customer_information[3]
        if subscription == '1':
            list_of_emails.append(customer_mail)
    return list_of_emails
    
   # list_customers = crm.get_list_customers()
    # # print("Email adresses of the subscribed customers:")
    # for customer_information in list_customers:
    #     table = BeautifulTable()
    #     table.columns_header = ["Email"]
    #     customer_mail = customer_information[-2]
    #     if customer_information[-1] == '1':
    #         table.append_row([f'{customer_mail}'])
    # print(table)

# def go_to_main_menu():
#     options = ["Exit program",
#                "Customer Relationship Management (CRM)",
#                "Sales",
#                "Human Resources"]
#     view.print_menu("Main menu", options)

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
    if option == 0:
        return
        # go_to_main_menu()
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
