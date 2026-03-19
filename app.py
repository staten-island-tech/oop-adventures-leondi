import time
cheddarstore = False
brokecontinue = "n"
brokecontinue = "n"
items_held = [
    {
        "buns": 8,
        "dogs": 8,
        "ketchup packets": 20,
        "mustard packets": 0,
    },
    {
        "A5 Wagyu": {
            "name": "A5 Wagyu",
            "stamina recovered": 30,
            "count": 0,
            "price": 50,
        },
        "Kraft Mac & Cheese": {
            "name": "Kraft Mac & Cheese",
            "stamina recovered": 20,
            "count": 0,
            "price": 30,
        },
        "Instant Noodles": {
            "name": "Instant Noodles",
            "stamina recovered": 10,
            "count": 5,
            "price": 15,
        },
        "Magic Money Cheddar": {
            "name": "Magic Money Cheddar",
            "stamina recovered": -15,
            "count": 0,
        },
    },
]
def guard(valid_choices, inputvar):
    if inputvar not in valid_choices:
        return False
    else:
        return True
iname = input("What is your name?")
class player:
    def __init__(self, name, money, stamina):
        self.name = name
        self.money = money
        self.stamina = stamina
    def eat(self):
        availabe_eat = []
        print("You sit down and have a meal.")
        for i in items_held[1]:
            if items_held[1][i]["count"] > 0:
                availabe_eat.append(items_held[1][i]["name"])
        if len(availabe_eat) > 1:
            print(f"You can eat {", ".join(availabe_eat)}.")
        elif len(availabe_eat) <= 1:
            print(f"You can eat some {availabe_eat[0]}.")
        food_chosen = input("What food would you like to eat? ")
        if guard(availabe_eat, food_chosen):
            if food_chosen == "Instant Noodles":
                print("You take the noodles out of their packaging.")
                time.sleep(2)
                print("You set the water to a boil.")
                time.sleep(2)
                print("...")
                time.sleep(2)
                print("...")
                time.sleep(2)
                print("...")
                time.sleep(2)
                print("It's boiling.")
                print("You put the noodles in the water.")
                time.sleep(2)
                print("...")
                time.sleep(2)
                print("...")
                time.sleep(2)
                print("...")
                time.sleep(2)
                print("You take the noodles out of the water.")
                time.sleep(2)
                print("You put the seasoning into the noodles.")
                time.sleep(2)
                if self.stamina >= 100:
                    items_held[1][food_chosen]["count"] -= 1
                    print(f"You eat the noodles. It doesn't matter though, you were already full stamina...")
                else:
                    print(f"You eat some {food_chosen}.")
                    self.stamina += items_held[1][food_chosen]["stamina recovered"]
                    items_held[1][food_chosen]["count"] -= 1
                    print(f"You're {items_held[1][food_chosen]["stamina recovered"]}% less tired.",
                    f" You now have {self.stamina}% stamina. You only have {items_held[1][food_chosen]["count"]} {food_chosen} now.")
            else:
                if self.stamina >= 100:
                    items_held[1][food_chosen]["count"] -= 1
                    print(f"You eat some {food_chosen}. It doesn't matter though, you were already full stamina...")
                else:
                    print(f"You eat some {food_chosen}.")
                    self.stamina += items_held[1][food_chosen]["stamina recovered"]
                    items_held[1][food_chosen]["count"] -= 1
                    print(f"You're {items_held[1][food_chosen]["stamina recovered"]}% less tired. ",
                    f"You now have {self.stamina}% stamina. You only have {items_held[1][food_chosen]["count"]} {food_chosen} now.")
        else:
            print("invalid")
    def foodstore(self):
        global brokecontinue
        totalcost = 0
        if cheddarstore == False:
            if brokecontinue != "y":
                print("You go to the grocery store.")
            for i in items_held[1]:
                try:
                    select = input(f"Do you want to buy any {items_held[1][i]["name"]}? (cost: ${items_held[1][i]["price"]}) (y/n) ")
                except KeyError:
                    break
                if guard(["y", "n"], select) and select == "y":
                    try:
                        foodnum = int(input(f"How many {items_held[1][i]["name"]} do you want? "))
                    except ValueError:
                        print("invalid")
                        break 
                    totalcost += items_held[1][i]["price"]*foodnum
                    if totalcost > self.money:
                        print("You can't buy that, you're too broke! ")
                        brokecontinue = input("Do you want to keep shopping? (y/n) ")
                        if brokecontinue == "y" and guard(["y", "n"], brokecontinue):
                            player.foodstore(user)
                        elif guard(["y", "n"], brokecontinue) == False:
                            print("invalid")
                            break 
                        else:
                            break
                    else:
                        items_held[1][i]["count"] += foodnum
                elif guard(["y", "n"], select) == False:
                    print("invalid")
                    break
            self.money -= totalcost
            print(f"Your total is ${totalcost}.")
            for i in items_held[1]:
                if items_held[1][i]["count"] > 0:
                    print(f"You now have {items_held[1][i]["count"]} {items_held[1][i]["name"]}.")
user = player(iname, 100, 100)
user.foodstore()