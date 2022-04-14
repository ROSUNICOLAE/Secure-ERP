from urllib.request import ProxyDigestAuthHandler


def get_biggest_revenue_product():
    transactions = [['l4x__QmU8r', 'k0_JUq+8hk', 'Bazooka', '843.4', '2017-04-30'], ['Hcik9!_o2T', 'P7+5Ggza!n',
                                                                                     'Sidewinder', '1500.0', '2018-02-02'], ['l4x__QmU8r', 'k0_JUq+8hk', 'Bazooka', '843.4', '2017-04-30']]
    
    faci o lista cu taate numele de produise
    produsuk care apare de cele mai multe ori devine variabila product
    produc = 'Sidewinder'
    price_index = 3
    total_price = 0
    for transaction in transactions :
        if transaction[2] == produc :
            total_price += float(transaction[price_index])
        else :
            continue
    print(total_price)


get_biggest_revenue_product()

#     # get the indexes of lists in transactions that have the same product name
#     indexes_same_product = []
#     for index in range(len(transactions)-1):
#         product = transactions[index][2]
#         if (index + 1) in range(len(transactions)-1):
#             try:
#                 if product.lower() == transactions[index+1][2].lower():
#                     print(product)
#                     index_product = transactions.index(transactions[index])
#                     indexes_same_product.append(index_product)
#             except IndexError:
#                 continue
#     print(indexes_same_product)
#     # transactions with the same product
#     transactions_that_have_the_same_product = []
#     for index in indexes_same_product:
#         transactions_that_have_the_same_product.append(transactions[index])
#     print(transactions_that_have_the_same_product)
#     # sum multiple products with the same name
#     sum_price_multiple_products = 0
#     for transaction in transactions_that_have_the_same_product:
#         price = transaction[-2]
#         sum_price_multiple_products += float(price)
#     print(sum_price_multiple_products)
#     # find the max price in big list
#     if len(transactions_that_have_the_same_product) > 1: 
#         name_of_multiple_product = transactions_that_have_the_same_product[0][2]
#         print(name_of_multiple_product)
        
        
        
        
        
    
# print(get_biggest_revenue_product())

        
            
        
        
        
    # revenues_float = [float(revenue) for revenue in revenues]
    # biggest_revenue = max(revenues_float)
    # print(biggest_revenue)
    # for transaction in transactions:
    #     for item in transaction:
    #         if item == str(biggest_revenue):
    #             index_transaction = transactions.index(transaction)
    # return transactions[index_transaction]
   


