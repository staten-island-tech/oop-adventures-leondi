import random
print("Welcome. You will have 4 highly trained operatives which you will have to direct across a mission.")
hack_name = input("Each operative specializes in a certain field. " \
"Your first operative will be the HACKER. They specialize in remote breaches of systems and providing digital assistance. " \
"What should your HACKER's name be? ")
ops_name = input("Your second operative will be the SPECIAL OP. They excel at taking out targets and directly entering missions to perform " \
"most of the physical work. What should your SPECIAL OP's name be? ")
sab_name = input("Your third operative will be the SABOTEUR. The SABOTEUR excels at stealth missions and being a useful mole in enemy territory. " \
"What should your SABOTEUR's name be? ")
mec_name = input("Your fourth and final operative will be the MECHANIC. The MECHANIC is a jack of all trades, " \
"and can be utilized in almost any situation. " \
"They are trained in hacking, stealth, as well as fighting. What should your MECHANIC's name be?  ")
pr = 100
captured = None
alias_first = ["John", "Bob", "James"]
alias_last = ["Smith", "Brown", "Johnson"]
class Operative:
    def __init__(self, name, num, type, phys_stat, tech_stat, stlh_stat, chrsm_stat, unlocked_list):
        self.name = name
        self.num = num
        self.type = type
        self.phys_stat = phys_stat
        self.tech_stat = tech_stat
        self.stlh_stat = stlh_stat
        self.chrsm_stat = chrsm_stat
        self.unlocked_list = unlocked_list
    def skills_showcase(self, statnum):
        if statnum == 1:
            if self.unlocked_list[0]:
                print(f"Your {self.type}, {self.name} has {self.phys_stat}/10 points in physical skills.")
            else:
                print(f"Your {self.type}, {self.name} has an unkown scoring in physical.")
        elif statnum == 2:
            if self.unlocked_list[1]:
                print(f"Your {self.type}, {self.name} has {self.tech_stat}/10 points in technical skills.")
            else:
                print(f"Your {self.type}, {self.name} has an unkown scoring in technical.")
        elif statnum == 3:
            if self.unlocked_list[2]:
                print(f"Your {self.type}, {self.name} has {self.stlh_stat}/10 points in stealth skills.")
            else:
                print(f"Your {self.type}, {self.name} has an unkown scoring in stealth.")
        elif statnum == 4:
            if self.unlocked_list[3]:
                print(f"Your {self.type}, {self.name} has {self.chrsm_stat}/10 points in charisma.")
            else:
                print(f"Your {self.type}, {self.name} has an unkown scoring in charisma.")
    def guard_act(self):
        if flashvar == "1":
            chance = (self.phys_stat*0.1)-0.05
            if chance >= random.random():
                print(f"{self.name} threw the flash... it hit! {team_name} quickly scramble into the bunker and lock the door behind them.")
                print(f"Turns out the {self.name} was {self.phys_stat}/10 skilled in physical capabilities.")
                if chance+0.05 >= random.random() and self.phys_stat < 10:
                    print(f"Thanks to the experience, {self.name}'s physical skills increased to {self.phys_stat}!")
            else:
                self.char_status = False
                operative_list.remove(self)
                print(f"{self.name} threw the flash... it missed! The guards were alerted and the alarm sounded. In the process, {self.name} was killed!")
                print(f"However, thanks to {self.name}'s sacrifice, the crew is able to gun down the remaining soldiers and sneak into the bunker. ")
        elif flashvar == "2":
            chance = (((self.phys_stat*0.1)-0.05) + (self.tech_stat*0.1)-0.05)/2
            if chance >= random.random():
                print(f"{self.name} attempts to gun down the guards... their shots hit clean! {team_name} quickly scramble into the bunker and lock the door behind them.")
                pr -= 10
                print(f"Turns out the {self.name} was {self.phys_stat}/10 skilled in physical capabilities and {self.tech_stat}/10 skilled in technical capabilities.")
                if chance+0.05 >= random.random() and self.tech_stat < 10:
                    self.tech_stat += 1
                    print(f"Thanks to the experience, {self.name}'s technical skills increased to {self.tech_stat}!")
                if chance+0.05 >= random.random() and self.phys_stat < 10:
                    self.tech_stat += 1
                    print(f"Thanks to the experience, {self.name}'s physical skills increased to {self.phys_stat}!")
            else:
                self.char_status = False
                operative_list.remove(self)
                if self.tech_stat > self.phys_stat:
                    print(f"{self.name} attempts to gun down the guards... thanks to their poor technical skills, they don't know how to undo the safety on the gun! " \
                          f"The guards were alerted and the alarm sounded. In the process, {self.name} was killed!")
                elif self.phys_stat >= self.tech_stat:
                    print(f"{self.name} attempts to gun down the guards... thanks to their poor physical skills, they miss most of the shots! " \
                          f"The guards were alerted and the alarm sounded. In the process, {self.name} was killed!")
                print(f"However, thanks to {self.name}'s sacrifice, the crew is able to gun down the remaining soldiers and sneak into the bunker. ")
    def mole(self):
        print(f"You have chosen your {self.type}, {self.name} to be your mole." \
              f" They apply to be a guard at the bunker under the alias {alias_first[random.randint(0, 2)]} {alias_last[random.randint(0,2)]}. ")
        chance = (((self.chrsm_stat*0.1)-0.05) + ((self.stlh_stat*0.1)-0.05))/2
        if chance < random.random():
            talk_c = input(f"{self.type} is under suspicion of being a spy! Do they attempt to smooth talk out of the situation? (y/n) ")
            if talk_c == "y":
                if chance < random.random():
                    print("The enemy belived it!")
                    if not self.unlocked_list[3]:
                        print(f"Turns out {self.name}'s charisma was {self.chrsm_stat}/10.")
                        self.unlocked_list[3] = True
                    print(f"{self.name} successfully infiltrated the bunker!")
                    print(f"{team_name} sneaks into the bunker undercover as a new cleaning crew. They're in!")
                else:
                    print(f"Turns out {self.name}'s charisma was {self.chrsm_stat}/10.")
                    self.unlocked_list[3] = True
                    print(f"{self.name}'s talking made him even more suspicious! The enemy placed them in prison! You'll have to rescue them later, or leave them there. ")
                    operative_list.remove(self)
                    captured = self
                    print("While the whole bunker is distracted trying to get information out of your spy, the rest of the crew is able to sneak in!")
            elif talk_c == "n":
                operative_list.remove(self)
                captured = self
                print(captured)
                print(f"{self.name}'s lack of explanation put them under suspicion even more! The enemy placed them in prison! You'll have to rescue them later, or leave them there. ")
                print("While the whole bunker is distracted trying to get information out of your spy, the rest of the crew is able to sneak in!")
        else:
            print(f"{self.name} successfully infiltrated the bunker!")
            print(f"{team_name} sneak into the bunker undercover as a new cleaning crew. They're in!")
    def bunchack(self):
        print(f"You have chosen your {self.type}, {self.name} to hack into the vault.")
        chance = (self.chrsm_stat*0.1)-0.05
        if chance < random.random():
            print(f"{self.name} attempts to breach the firewall... they fail! The enemy instantly locks onto their location and eliminates them. {self.name} died!")
            operative_list.remove(self)
        else:
            print(f"{self.name} successfully hacked into the vault!")
            if not self.unlocked_list[1]:
                print(f"Turns out {self.name}'s is {self.chrsm_stat}/10 skilled in technical skills.")
                self.unlocked_list[1] = True
            if chance+0.05 >= random.random() and self.tech_stat < 10:
                self.tech_stat += 1
                print(f"Thanks to the experience, {self.name}'s technical skills increased to {self.tech_stat}!")
            print(f"{team_name} are in the bunker! They copy the codes onto a hard drive and destroy the server room with a grenade. The whole bunker is alerted! ")
def alive_select():
    if len(operative_list) == 1:
        return "(1) "
    elif len(operative_list) == 2:
        return "(1/2) "
    elif len(operative_list) == 3:
        return "(1/2/3) "
    elif len(operative_list) == 4:
        return "(1/2/3/4) "
hacker = Operative(hack_name, "1",  "HACKER", random.randint(2, 5), random.randint(6, 8), random.randint(3, 5), random.randint(2, 6), [False, False, False, False])
special_op = Operative(ops_name, "2", "SPECIAL OP", random.randint(6, 8), random.randint(3, 6), random.randint(4, 6), random.randint(1, 3), [False, False, False, False])
saboteur = Operative(sab_name, "3", "SABOTEUR", random.randint(3, 5), random.randint(1, 3), random.randint(6, 8), random.randint(5, 7), [False, False, False, False])
mechanic = Operative(mec_name, "4", "MECHANIC", random.randint(3, 5), random.randint(3, 5), random.randint(3, 5), random.randint(3, 5), [False, False, False, False])
team_name = input("What should your team name be? ")
operative_list = [hacker, special_op, saboteur, mechanic]
print("Your mission will be to retrive nuclear codes that will be used to launch ICBMs towards some of the most populated cities in the world.")
bunk_choice = input("These nuclear codes are stored in an extremely secure bunker. You can either breach the bunker by force or infiltrate it. (1/2) ")
if bunk_choice == "1":
    print("You have chosen to breach the bunker by force. Your mission will consist of 1) Taking out the guards by the entrance without triggering the alarm ",
          "2) Succesfully obtain the code for the door to the nuclear code servers in order to be able to download them or destroy them altogether. ",
          "3) Destroy the codes (or bring them back to base). ")
    flashvar = input(f"{team_name} arrives at the site of the bunker. They'll need to take out the small army of guards in the front. " \
                         "Should they throw a flashbang to distract the guards, or attempt to gun them down? (1/2) ")
    if flashvar == "1":
        print("You'll probably need someone highly skilled physically to throw the flashbang properly.")
        for person in operative_list:
            person.skills_showcase(1)
        char_choice = input(f"Who should throw the flash? {alive_select()}")
        for person in operative_list: 
            if person.num == char_choice:
                person.guard_act()
    elif flashvar == "2":
        print("You'll probably need someone highly skilled in phyiscal and technical to succesfully take out the guards.")
        for person in operative_list:
            person.skills_showcase(1)
            person.skills_showcase(2)
        char_choice = input(f"Who should attempt to gun down the guards? {alive_select()}")
        for person in operative_list: 
            if person.num == char_choice:
                person.guard_act()
elif bunk_choice == "2":
    print("You have chosen to breach the bunker by infiltrating it. Your mission will consist of 1) Planting an inside man to allow your other operatives to sneak in. ",
          "2) Hack into the vualt with the codes to open the door. ",
          "3) Retrive the nuclear codes. ")
    print("First, you'll have to plant a mole to be able to sneak past the intitial defenses. Someone with high charisma is ideal.")
    for person in operative_list:
        person.skills_showcase(4)
    ins_char = input(f"Who should be the mole? {alive_select()}")
    for person in operative_list: 
        if person.num == ins_char:
            person.mole()
    if captured == None:
        print("Now that the crew is in, you'll have to hack into the secure vault with the codes. Someone who is highly skilled in tech is perfect for this.")
    for person in operative_list:
        person.skills_showcase(2)
    ins_char = input(f"Who should hack into the system? {alive_select()}")
    for person in operative_list: 
        if person.num == ins_char:
            person.bunchack()