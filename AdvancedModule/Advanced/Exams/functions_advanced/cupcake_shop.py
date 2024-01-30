def stock_availability(list_of_products, command, *args):
    if command == 'delivery':
        for product in args:
            list_of_products.append(product)

    elif command == 'sell':
        if not args:
            list_of_products.pop(0)
        else:
            if len(args) == 1 and isinstance(args[0], int):
                for count in range(args[0]):
                    list_of_products.pop(0)
            else:
                for product in args:
                    for prod in list_of_products[::-1]:
                        if product == prod:
                            list_of_products.remove(product)

    return list_of_products


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
