""" sushi_orders = [
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
for order in sushi_orders:
    if order["name"] not in recipt:
        recipt[order["name"]] = {"price": order["price"], "count": 1}
    else:
        recipt[order["name"]]["count"] += 1
for sushi, value in recipt.items():
    print(sushi, "quantity:", value["count"], "price:", value["count"]*value["price"]) """
""" 
wards = {
    "Cardiology":  ["Alice", "Bob", "Carol"],
    "Neurology":   ["Diana", "Eve"],
    "Orthopedics": ["Frank", "Grace", "Hank"],
    "Oncology":    ["Ivy", "Bob"]
}

staff = {}
for ward, list in wards.items():
    for person in list:
        if person not in staff:
            staff[person] = {
                "wards": [ward]
            }
        else:
            staff[person]["wards"].append(ward)
print(staff)
 """
phonenum = {
    2: ["a", "b", "c"],
    3: ["d", "e", "f"],
    4: ["g", "h", "i"],
    5: ["j", "k", "l"],
    6: ["m", "n", "o"],
    7: ["p", "q", "r", "s"],
    8: ["t", "u", "v"],
    9: ["w", "x", "y", "z"]
}
def marko(wordlist, nums_input):
    for word in wordlist:
        for letter in range(len(word)):
            if letter in phonenum[nums_input]