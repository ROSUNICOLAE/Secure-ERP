from tabulate import tabulate
from model import data_manager, util
from view import terminal as view


def print_menu(title, list_options):
    """Prints options in standard menu format like this:

    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """
    print(title)
    for index in range(len(list_options)+1):
        if (index + 1) in range(len(list_options)):
            print(f'({index + 1}) {list_options[index + 1]}')
    print(f'({0}) {list_options[0]}')


def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    pass


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    pass


# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/
def print_table(table):
    """Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
    """
    HEADERS = ["id", "name", "email", "subscribed"]
    print(tabulate(table, HEADERS, tablefmt="fancy_grid",
      colalign=("center",), numalign="center"))


def get_input(label):
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """
    label = int(input(f'{label} : '))
    return label


def get_inputs():
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    labels = []
    new_client_id = util.generate_id(number_of_small_letters=4,
                                number_of_capital_letters=2,
                                number_of_digits=2,
                                number_of_special_chars=2,
                                allowed_special_chars=r"_+-!")
    labels.append(new_client_id)
    labels.append(input("Add a name: "))
    labels.append(input("Add an email adress: "))
    labels.append(input(
        "Is subscribed to the newsletter? Enter 1 for 'yes', 0 for 'no': "))
    return labels


def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    print(message)
