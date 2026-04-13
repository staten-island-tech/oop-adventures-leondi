import random
print("Welcome. You will have 4 highly trained operatives which you will have to direct across 3 unique missions.")
hack_name = input("Each operative specializes in a certain field. " \
"Your first operative will be the HACKER. They specialize in remote breaches of systems and providing digital assistance. " \
"What should your HACKER's name be? ")
ops_name = input("Your second operative will be the SPECIAL OP. They excel at taking out targets and directly entering missions to perform " \
"most of the physical work. What should your SPECIAL OP's name be? ")
sab_name = input("Your third operative will be the SABOTEUR. The SABOTEUR excels at stealth missions and being a useful mole in enemy territory. " \
"What should your SABOTEUR's name be? ")
mec_name = input("Your fourth and final operative will be the MECHANIC. The MECHANIC is a jack of all trades, " \
"and can be utilized in almost any situation. " \
"They are trained in hacking, stealth, as well as fighting. What should your MECHANIC's name be? ")
class Operative:
    def __init__(self, name, type, phys_stat, tech_stat, stlh_stat, chrsm_stat, unlocked_list):
        self.name = name
        self.type = type
        self.phys_stat = phys_stat
        self.tech_stat = tech_stat
        self.stlh_stat = stlh_stat
        self.chrsm_stat = chrsm_stat
        self.unlocked_list = unlocked_list
    def skills_showcase(skill):
        for i in operative_list:
            print(f"Your {i}")
"""     def guard_act(guard_choice):
        if guard_choice == "1":
                 """

hacker = Operative(hack_name, "HACKER", random.randint(2, 5), random.randint(6, 8), random.randint(3, 5), random.randint(2, 6))
print(hacker)
special_op = Operative(ops_name, "SPECIAL OP", random.randint(6, 8), random.randint(3, 6), random.randint(4, 6), random.randint(1, 3))
saboteur = Operative(sab_name, "SABOTEUR", random.randint(3, 5), random.randint(1, 3), random.randint(6, 8), random.randint(5, 7))
mechanic = Operative(mec_name, "MECHANIC", random.randint(3, 5), random.randint(3, 5), random.randint(3, 5), random.randint(3, 5))
team_name = input("What should your team name be? ")
operative_list = [hacker, special_op, saboteur, mechanic]
pr = 100
print("Your first mission will be to retrive nuclear codes that will be used to launch ICBMs towards some of the most populated cities in the world.")
bunk_choice = input("These nuclear codes are stored in an extremely secure bunker. You can either breach the bunker by force or infiltrate it. (1/2) ")
if bunk_choice == "1":
    print("You have chosen to breach the bunker by force. Your mission will consist of 1) Taking out the guards by the entrance without triggering the alarm ",
          "2) Succesfully obtain the code for the door to the nuclear code servers in order to be able to download them or destroy them altogether. " \
          "3) Destroy the codes (or bring them back to base). ")
    guard_choice = input(f"{team_name} arrives at the site of the bunker. They'll need to take out the small army of guards in the front. " \
                         "Should they throw a flashbang to distract the guards, or attempt to gun them down? (1/2) ")
    Operative.guard_act(guard_choice)