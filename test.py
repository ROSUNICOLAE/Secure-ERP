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
   

print(get_biggest_revenue())