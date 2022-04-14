def get_biggest_revenue_product(transactions):

    products = []
    for transaction in transactions:
        products.append(transaction[2])
    # print(products)
    #check for duplicates
    unique_products = set(products)
    if len(products) == len(unique_products):
        print("no duplicate product, max din celalalta functie de returnat")
    else:
        print("de aflat care sunt duplicatele")
        filter_products = []
        multiple_products = []
        for product in products:
            if product not in filter_products:
                filter_products.append(product)
            else:
                multiple_products.append(product)
        print(multiple_products)
        products_with_duplicates = list(set(multiple_products))
        print(products_with_duplicates)
        
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
        print(transaction_multiple_products0)
        sum0 = 0
        for transaction in transaction_multiple_products0:
            price = transaction[-2]
            sum0 += float(price)
        print(sum0)
        sum1 = 0
        for transaction in transaction_multiple_products1:
            price = transaction[-2]
            sum1 += float(price)
        print(sum1)
        sum2 = 0
        for transaction in transaction_multiple_products2:
            price = transaction[-2]
            sum2 += float(price)
        print(sum2)
        sum3 = 0
        for transaction in transaction_multiple_products3:
            price = transaction[-2]
            sum3 += float(price)
        print(sum3)
        sum4 = 0
        for transaction in transaction_multiple_products4:
            price = transaction[-2]
            sum4 += float(price)
        print(sum4)
        sum_max = max(sum0, sum1, sum2, sum3, sum4)
        print(sum_max)
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
        
        
        
        

        # for transaction in transactions_multiple_products:
        #     for i in range(len(products_with_duplicates)):
        #         if transaction[2] == products_with_duplicates[i]:
        #             product_with_duplicate_i.append(transaction)
        #             # product_sum += float(transaction[1][-2])
        #         else:
        #             i += 1
        # print(product_sum)
                
            
print(get_biggest_revenue_product(transactions = [['l4x__QmU8r', 'k0_JUq+8hk', 'Bazooka', '843.4', '2017-04-30'],
                                                  ['Hcik9!_o2T', 'P7+5Ggza!n', 'Sidewinder2', '1500.0', '2018-02-02'],\
                                                  ['N41z-Dgcz-', 'k0_JUq+8hk', 'Bazooka', '843.4', '2018-05-24'],\
    ['TiA9s!8n-c', 'Vans', 'otisu', '83.22', '2022-04-09'],
    ['TiA9s!8n-c', 'Vans', 'otis', '1223.22', '2022-04-09'],
    ['Hcik9!_o2T', 'P7+5Ggza!n', 'Sidewinder', '1500.0', '2018-02-02'],
    ['TiA9s!8n-c', 'Vans', 'eee', '1223.22', '2022-04-09'],
    ['TiA9s!8n-c', 'Vans', 'shhhh', '1223.22', '2022-04-09'],
    ['TiA9s!8n-c', 'Vans', 'oll', '1223.22', '2022-04-09']]))
    










