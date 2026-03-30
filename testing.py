sushi_orders = [
    {"name": "California Roll", "price": 8},
    {"name": "Spicy Tuna Roll", "price": 10},
    {"name": "Salmon Nigiri", "price": 6},
    {"name": "California Roll", "price": 8},
    {"name": "Dragon Roll", "price": 12},
    {"name": "Spicy Tuna Roll", "price": 10},
    {"name": "Miso Soup", "price": 4},
    {"name": "Edamame", "price": 5},
    {"name": "Salmon Nigiri", "price": 6},
    {"name": "California Roll", "price": 8}
]
recipt = {}
for order in range(len(sushi_orders)):
    if order["name"] not in recipt:
        recipt[order["name"]] = {"price": order["price"], "count": 1}
    elif sushi_orders[order]["name"] in recipt:
        recipt[order["name"]]["quantity"] += 1
print(recipt)