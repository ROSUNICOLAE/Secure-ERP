# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/


# def print_table(table):
#    """Prints tabular data like above.

#     Args:
#         table: list of lists - the table to print out
#     """
#     pass

from tabulate import tabulate
HEADERS = ["id", "name", "email", "subscribed"]

table = [['pF5v4wG_e_', 'Dr. Strangelove',   'strangelove@rgv453.grer',     '1'], \
         ['k0_JUq+8hk', 'Kim',                  'supremeleader@dfs.vfsdfv', '0'], \
         ['l4x__QmU8r', 'Unknown',                   '---',                 '0'], \
         ['P7+5Ggza!n', 'Known',                         'ping@me',          '1']]

# flat_list = [item for sublist in table for item in sublist]
# longest_string = (max(flat_list, key=len))

flat_list = [item for sublist in table for item in sublist]
print(flat_list)
print(tabulate(table, HEADERS, tablefmt="fancy_grid", colalign=("center",), numalign="center"))


