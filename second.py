""" from app import flashvar, team_name, operative_list, win """
import random 
class Operative:
    def __init__(self, name, num, type, phys_stat, tech_stat, stlh_stat, chrsm_stat, unlocked_list, captured):
        self.name = name
        self.num = num
        self.type = type
        self.phys_stat = phys_stat
        self.tech_stat = tech_stat
        self.stlh_stat = stlh_stat
        self.chrsm_stat = chrsm_stat
        self.unlocked_list = unlocked_list
        self.captured = captured
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
    def codeget(self):
            global code
            chance = (((self.chrsm_stat*0.1)-0.05) + ((self.phys_stat*0.1)-0.05))/2
            if chance > random.random():
                code = random.randint(1000,9999)
                print(f"{self.name} is successful in getting the code from the worker he interrogated! The code is {code}.")
                if self.unlocked_list[0] == False:
                    print(f"Turns out {self.name}'s charisma was {self.phys_stat}/10.")
                    self.unlocked_list[0] = True
                if self.unlocked_list[3] == False:
                    print(f"Turns out {self.name}'s stealth was {self.chrsm_stat}/10.")
                    self.unlocked_list[3] = True
                self.unlocked_list[1] = True
                if chance+0.05 >= random.random() and self.chrsm_stat < 10:
                    self.chrsm_stat += 1
                    print(f"Thanks to the experience, {self.name}'s charisma skills increased to {self.chrsm_stat}!")
            else:
                print(f"{self.name} takes too long to interrogate the employee and the crew is caught and captured. ")
                print("FAILED")
                quit()
    def vualtentry(self):
        code_input = input("What is the code? ")
        if code_input == code:
            print("The team enters the vault. They copy down the codes onto a drive and destroy the originals. ")
        else:
            print("Because of your inability to memorize a 4 digit number, the entire crew gets captured. ")
            print("FAILED")
            quit()
    def mole(self):
        print(f"You have chosen your {self.type}, {self.name} to be your mole." \
              f" They apply to be a guard at the bunker under the alias {alias_first[random.randint(0, 2)]} {alias_last[random.randint(0,2)]}. ")
        chance = (((self.chrsm_stat*0.1)-0.05) + ((self.stlh_stat*0.1)-0.05))/2
        if chance < random.random():
            talk_c = input(f"{self.type} is under suspicion of being a spy! Do they attempt to smooth talk out of the situation? (y/n) ")
            if talk_c == "y":
                if chance > random.random():
                    print("The enemy belived it!")
                    if self.unlocked_list[3] == False:
                        print(f"Turns out {self.name}'s charisma was {self.chrsm_stat}/10.")
                        self.unlocked_list[3] = True
                    if self.unlocked_list[2] == False:
                        print(f"Turns out {self.name}'s stealth was {self.stlh_stat}/10.")
                        self.unlocked_list[2] = True
                    print(f"{self.name} successfully infiltrated the bunker!")
                    print(f"{team_name} sneaks into the bunker undercover as a new cleaning crew. They're in!")
                else:
                    if self.unlocked_list[3] == False:
                        print(f"Turns out {self.name}'s charisma was {self.chrsm_stat}/10.")
                        self.unlocked_list[3] = True
                    if self.unlocked_list[2] == False:
                        print(f"Turns out {self.name}'s stealth was {self.stlh_stat}/10.")
                        self.unlocked_list[2] = True
                    print(f"{self.name}'s talking made him even more suspicious! The enemy placed them in prison! You'll have to rescue them later, or leave them there. ")
                    self.captured = True
                    print("While the whole bunker is distracted trying to get information out of your spy, the rest of the crew is able to sneak in!")
            elif talk_c == "n":
                self.captured = True
                print(f"{self.name}'s lack of explanation put them under suspicion even more! The enemy placed them in prison! You'll have to rescue them later, or leave them there. ")
                print("While the whole bunker is distracted trying to get information out of your spy, the rest of the crew is able to sneak in!")
        else:
            print(f"{self.name} successfully infiltrated the bunker!")
            if self.unlocked_list[3] == False:
                print(f"Turns out {self.name}'s charisma was {self.chrsm_stat}/10.")
                self.unlocked_list[3] = True
            if self.unlocked_list[2] == False:
                print(f"Turns out {self.name}'s stealth was {self.stlh_stat}/10.")
            self.unlocked_list[2] = True
            print(f"{team_name} sneak into the bunker undercover as a new cleaning crew. They're in!")
    def bunchack(self):
        print(f"You have chosen your {self.type}, {self.name} to hack into the vault.")
        for person in operative_list:
            if person.captured == True:
                print(f"Currently, {person.name} is captured in the enemy's prison. Rescuing them requires opening the prsion door via hack. This will take some time and skills, and you can risk being found.")
                rescuechoice = input(f"Should {self.name} attempt to break out {person.name}? (y/n) ")   
                if rescuechoice == "y":
                    self.breakout()     
        chance = (self.tech_stat*0.1)-0.05
        if chance < random.random():
            print(f"{self.name} attempts to breach the firewall... they fail! The enemy instantly locks onto their location and eliminates them. {self.name} died!")
            print(f"Instead, the team chooses to blow up the vualt with c4 and destroy the codes altogether.")
            operative_list.remove(self)
        else:
            print(f"{self.name} successfully hacked into the vault!")
            if not self.unlocked_list[1]:
                print(f"Turns out {self.name}'s is {self.tech_stat}/10 skilled in technical skills.")
                self.unlocked_list[1] = True
            if chance+0.05 >= random.random() and self.tech_stat < 10:
                self.tech_stat += 1
                print(f"Thanks to the experience, {self.name}'s technical skills increased to {self.tech_stat}!")
            print(f"{team_name} are in the bunker! They copy the codes onto a hard drive and destroy the server room with a grenade. The whole bunker is alerted! ")
    def breakout(self):
        chance = (self.tech_stat*0.1)-0.05
        if chance < random.random():
            print(f"{self.name} attempts to open the prison door... they fail! The enemy tracked their computer and found the entire crew and captured them!")
            print("FAILED")
            quit()
        else:
            print(f"{self.name} successfully hacked in the prison and opened the door, allowing the prisoner to escape!")
            for person in operative_list:
                if person.captured:
                    person.captured = False
            if not self.unlocked_list[1]:
                print(f"Turns out {self.name}'s is {self.tech_stat}/10 skilled in technical skills.")
                self.unlocked_list[1] = True
            if chance+0.05 >= random.random() and self.tech_stat < 10:
                self.tech_stat += 1
                print(f"Thanks to the experience, {self.name}'s technical skills increased to {self.tech_stat}!")
    def escape(self):
        print(f"You have chosen your {self.type}, {self.name} to pilot the heli. ")
        chance = (self.tech_stat*0.1)-0.05
        if chance < random.random():
            print(f"{self.name} fails to pilot the heli properly and flies into a nearby mountain! The heli explodes and the whole crew dies. ")
            print("FAILED")
            quit()
        else:
            print(f"{self.name} is sucsesfull and the crew escapes!")
            win()