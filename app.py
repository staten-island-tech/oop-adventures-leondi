items_held = [
    {
        "buns": 8
        "dogs": 8
        "ketchup packets": 20
        "mustard packets": 0
    },
    {
        "A5 Wagyu": {
            "name": "A5 Wagyu"
            "stamina recovered": 30
            "count": 0
        }
        "Kraft Mac & Cheese": {
            "name": "Kraft Mac & Cheese"
            "stamina recovered": 20
            "count": 0
        }
        "Instant Noodles": {
            "name": "Instant Noodles"
            "stamina recovered": 10
            "count": 5
        }
        "Magic Money Cheddar": {
            "name": "Magic Money Cheddar"
            "stamina recovered": -15
            "count": 0
        }
    }
]
class player:
    def __init__(self, name, money, inventory, stamina):
        self.name = name
        self.money = money
        self.inventory = inventory
        self.stamina = stamina
    def eat(self, stamina):
        availabe_eat = []
        print("You sit down and have a meal.")
        for i in items_held[1][i]["count"]:
            if items_held[1][i]["count"] > 0:
                availabe_eat.append(items_held[1][i]["name"])
        print("")
        self.stamina += stamina*items_held[1]
        print()
class store:
    def __init__(self, items):
        self.items = items