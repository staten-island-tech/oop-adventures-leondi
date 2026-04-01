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
    "a": 2,
    "b": 2,
    "c": 2,
    "d": 3,
    "e": 3,
    "f": 3,
    "g": 4,
    "h": 4,
    "i": 4,
    "j": 5,
    "k": 5,
    "l": 5,
    "m": 6,
    "n": 6,
    "o": 6,
    "p": 7,
    "q": 7, 
    "r": 7,
    "s": 7,
    "t": 8,
    "u": 8,
    "v": 8,
    "w": 9, 
    "x": 9, 
    "y": 9,
    "z": 9,
}
def marko(wordlist, nums_input):
    badword = []
    for word in wordlist:
        thing = [*word]
        for char in range(len(thing)):
            if phonenum[word[char]] != nums_input[char]:
                badword.append(word)
    print(badword)
marko(["tomo","mono","dak"], [6, 6,6,6])