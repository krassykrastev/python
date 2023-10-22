def shop_from_grocery_list(budget, products, *datas):

    for data in datas:
        product = data[0]
        price = data[1]
        if product in products:
            if budget - price < 0:
                break

            products.remove(product)
            budget -= price

    if products:
        return f"You did not buy all the products. Missing products: {', '.join(products)}."
    return f"Shopping is successful. Remaining budget: {budget:.2f}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))