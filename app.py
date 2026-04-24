import random
from second import Operative
print("Welcome. You will have 4 highly trained operatives which you will have to direct across a mission. Each one has a specific skillset that you will have to utilize.")
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
alive_list = [1,2,3,4]
alias_first = ["John", "Bob", "James"]
alias_last = ["Smith", "Brown", "Johnson"]
def guard(valid_choice, user_input):
    if user_input in valid_choice:
        return True
    else:
        return False
def ifcaptured():
    output = True
    for person in operative_list:
        if person.captured:
            output = False
    if output:
        return True
    else:
        return False
def alive_select():
    global alive_list
    if len(operative_list) == 1:
        alive_list = [1]
        return "(1) "
    if len(operative_list) == 2 and ifcaptured():
        alive_list = [1, 2]
        return "(1/2) "
    elif len(operative_list) == 2:
        alive_list = [1]
        return "(1) "
    if len(operative_list) == 3 and ifcaptured():
        alive_list = [1, 2, 3]
        return "(1/2/3) "
    elif len(operative_list) == 3:
        alive_list = [1, 2]
        return "(1/2) "
    if len(operative_list) == 4 and ifcaptured():
        alive_list = [1, 2, 3, 4]
        return "(1/2/3/4) "
    elif len(operative_list) == 4:
        alive_list = [1, 2, 3]
        return "(1/2/3) "
def win():
    ranklist = ["C", "B", "A", "S"]
    numalive=0
    for person in operative_list:
        if person.captured==False:
            numalive+=1
    print(f"You have successfully completed the mission. Your rank is {ranklist[numalive-1]}.")
    print("WIN!")
    quit()
hacker = Operative(hack_name, "1",  "HACKER", random.randint(2, 5), random.randint(6, 8), random.randint(3, 5), random.randint(2, 6), [False, False, False, False], False)
special_op = Operative(ops_name, "2", "SPECIAL OP", random.randint(6, 8), random.randint(3, 6), random.randint(4, 6), random.randint(1, 3), [False, False, False, False], False)
saboteur = Operative(sab_name, "3", "SABOTEUR", random.randint(3, 5), random.randint(1, 3), random.randint(6, 8), random.randint(5, 7), [False, False, False, False], False)
mechanic = Operative(mec_name, "4", "MECHANIC", random.randint(3, 5), random.randint(3, 5), random.randint(3, 5), random.randint(3, 5), [False, False, False, False], False)
team_name = input("What should your team name be? ")
operative_list = [hacker, special_op, saboteur, mechanic]
print("Your mission will be to retrive nuclear codes that will be used to launch ICBMs towards some of the most populated cities in the world.")
bunk_choice = input("These nuclear codes are stored in an extremely secure bunker. You can either breach the bunker by force or infiltrate it. (1/2) ")
if guard(["1","2"], bunk_choice) != True:
    print("invalid.")
    while (alive_list, bunk_choice) != True:
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
        if guard(alive_list, char_choice) != True:
            print("invalid.")
            while (alive_list, char_choice) != True:
                char_choice = input(f"Who should throw the flash? {alive_select()}")
        for person in operative_list: 
            if operative_list.index(person)+1 == int(char_choice):
                person.guard_act()
    elif flashvar == "2":
        print("You'll probably need someone highly skilled in phyiscal and technical to succesfully take out the guards.")
        for person in operative_list:
            if person.captured == False:
                person.skills_showcase(1)
                person.skills_showcase(2)
        char_choice = input(f"Who should attempt to gun down the guards? {alive_select()}")
        if guard(alive_list, char_choice) != True:
            print("invalid.")
            while (alive_list, char_choice) != True:
                char_choice = input(f"Who should attempt to gun down the guards? {alive_select()}")
        for person in operative_list: 
            if operative_list.index(person)+1 == int(char_choice):
                person.guard_act()
    print(f"{team_name} are in the bunker. They'll have to get the code for the vault from one of the personnel, or attempt to hack in the vault. ")
    code_choice = input("Should the team attempt to get the code themselves or hack into the vault? (1/2) ")
    if code_choice == "1":
        print("Someone who is intimidating should be best to get the code from one of the personnel (high charisma + physical).")
        for person in operative_list:
            if person.captured == False:
                person.skills_showcase(1)
                person.skills_showcase(4)
        pers_choice = input(f"Who should attempt the task? {alive_select()}")
        if guard(alive_list, pers_choice) != True:
            print("invalid.")
            while (alive_list, pers_choice) != True:
                pers_choice = input(f"Who should attempt the task? {alive_select()}")
        for person in operative_list: 
            if operative_list.index(person)+1 == int(pers_choice):
                person.codeget()
        person.vualtentry()
    elif code_choice == "2":
        print("You'll have to hack into the secure vault with the codes. Someone who is highly skilled in tech is perfect for this.")
        for person in operative_list:
            if person.captured == False:
                person.skills_showcase(2)
        ins_char = input(f"Who should hack into the system? {alive_select()}")
        if guard(alive_list, ins_char) != True:
            print("invalid.")
            while (alive_list, ins_char) != True:
                ins_char = input(f"Who should hack into the system? {alive_select()}")
        for person in operative_list: 
            if operative_list.index(person)+1 == int(ins_char):
                person.bunchack()
    print("A small army of guards are chasing the team down! They escape to their helicopter. Someone with high technical skills will be best for this.")
    for person in operative_list:
        if person.captured == False:
            person.skills_showcase(1)
    helichoice = input(f"Who should attempt the task? {alive_select()}")
    if guard(alive_list, char_choice) != True:
            print("invalid.")
            while (alive_list, helichoice) != True:
                helichoice = input(f"Who should attempt the task? {alive_select()}")
    for person in operative_list: 
        if operative_list.index(person)+1 == int(helichoice):
            person.escape()
elif bunk_choice == "2":
    print("You have chosen to breach the bunker by infiltrating it. Your mission will consist of 1) Planting an inside man to allow your other operatives to sneak in. ",
          "2) Hack into the vault with the codes to open the door. ",
          "3) Retrive the nuclear codes. ")
    print("First, you'll have to plant a mole to be able to sneak past the intitial defenses. Someone with high charisma and stealth is ideal.")
    for person in operative_list:
        if person.captured == False:
            person.skills_showcase(4)
            person.skills_showcase(3)
    ins_char = input(f"Who should be the mole? {alive_select()}")
    if guard(alive_list, ins_char) != True:
        print("invalid.")
        while (alive_list, ins_char) != True:
            ins_char = input(f"Who should be the mole? {alive_select()}")
    for person in operative_list: 
        if operative_list.index(person)+1 == int(ins_char):
            person.mole()
    print("Now that the crew is in, you'll have to hack into the secure vault with the codes. Someone who is highly skilled in tech is perfect for this.")
    for person in operative_list:
        if person.captured == False:
            person.skills_showcase(2)
    ins_char = input(f"Who should hack into the system? {alive_select()}")
    if guard(alive_list, ins_char) != True:
        print("invalid.")
        while (alive_list, ins_char) != True:
            ins_char = input(f"Who should hack into the system? {alive_select()}")
    for person in operative_list: 
        if operative_list.index(person)+1 == int(ins_char):
            person.bunchack()
    print("A small army of guards are chasing the team down! They escape to their helicopter. Someone with high technical skills will be best for this.")
    for person in operative_list:
        if person.captured == False:
            person.skills_showcase(2)
    helichoice = input(f"Who should attempt the task? {alive_select()}")
    if guard(alive_list, helichoice) != True:
        print("invalid.")
        while (alive_list, helichoice) != True:
            helichoice = input(f"Who should attempt the task? {alive_select()}")
    for person in operative_list: 
        if operative_list.index(person)+1 == int(helichoice):
            person.escape()