def get_biggest_revenue():
    transactions = [['l4x__QmU8r', 'k0_JUq+8hk', 'Bazooka', '843.4', '2017-04-30'], ['Hcik9!_o2T', 'P7+5Ggza!n', 'Sidewinder', '1500.0', '2018-02-02'], ['N41z-Dgcz-', 'k0_JUq+8hk', 'Bazooka', '843.4',
                                                                                                                                      '2018-05-24'], ['TiA9s!8n-c', 'Vans', 'otis', '83.22', '2022-04-09'], ['TiA9s!8n-c', 'Vans', 'otis', '1223.22', '2022-04-09'], ['TiA9s!8n-c', 'Vans', 'otis', '223.22', '2022-04-09']]
    revenues = []
    for transaction in transactions:
        revenue = transaction[-2]
        revenues.append(revenue)
    revenues_float = [float(revenue) for revenue in revenues]
    biggest_revenue = max(revenues_float)
    print(biggest_revenue)
    for transaction in transactions:
        for item in transaction:
            if item == str(biggest_revenue):
                index_transaction = transactions.index(transaction)
    return transactions[index_transaction]
   


# Python program to print
# colored text and background
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))
 
prCyan("Hello World, ")
prYellow("It's")
prGreen("Geeks")
prRed("For")
prGreen("Geeks")