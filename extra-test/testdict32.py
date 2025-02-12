print("deneme")
def calculate_total_price(cart, prices):
    total_price = 0
    for item, quantity in cart.items():
        if item in prices:
            total_price += prices[item] * quantity
    return total_price

product_prices = {"apple": 1, "banana": 0.5, "orange": 0.75}
shopping_cart = {"apple": 3, "banana": 2, "orange": 4}
total_cost = calculate_total_price(shopping_cart, product_prices)
print("deneme")