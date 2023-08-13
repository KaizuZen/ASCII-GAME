# Extremely messy code, One of my first projects.

import time , os , random

run = True
menu = True
play = False
rules = False
key = False
fight = False
standing = True
buy = False
speak = False
boss = False

hp = 50
hpmax = 100
atk = 8
pot = 5
elix = 2
gold = 100
x = 0
y = 0

       #  x = 0       x = 1       x = 2       x = 3       x = 4       x = 5         x = 6
map = [["plains",   "plains",   "plains",   "plains",   "forest", "mountain",       "cave"],    # y = 0
       ["forest",   "forest",   "forest",   "forest",   "forest",    "hills",   "mountain"],    # y = 1
       ["forest",   "fields",   "bridge",   "plains",    "hills",   "forest",      "hills"],    # y = 2
       ["plains",     "shop",     "town",    "mayor",   "plains",    "hills",   "mountain"],    # y = 3
       ["plains",   "fields",   "fields",   "plains",    "hills", "mountain",   "mountain"]]    # y = 4

y_len = len(map)-1
x_len = len(map[0]) -1

# Some Places
biome = {
    "plains": {
        "t": "PLAINS",
        "e": True},
    "forest": {
        "t": "WOODS",
        "e": True},
    "fields": {
        "t": "FIELDS",
        "e": False},
    "bridge": {
        "t": "BRIGE",
        "e": True},
    "town": {
        "t": "TOWN CENTRE",
        "e": False},
    "shop": {
        "t": "SHOP",
        "e": False},
    "mayor": {
        "t": "MAYOR",
        "e": False},
    "cave": {
        "t": "CAVE",
        "e": False},
    "mountain": {
        "t": "MOUNTAIN",
        "e": True},
    "hills": {
        "t": "HILLS",
        "e": True,
    }
}

e_list = ["Goblin", "Orc", "Slime"]

mobs = {
    "Goblin": {
        "ehp": 15,
        "at": 3,
        "go": 8
    },
    "Orc": {
        "ehp": 35,
        "at": 5,
        "go": 18
    },
    "Slime": {
        "ehp": 30,
        "at": 2,
        "go": 12
    },
    "Dragon": {
        "ehp": 100,
        "at": 8,
        "go": 100
    }
}


# Some functions:
def save():
    player_list = [
        name,
        str(hp),
        str(atk),
        str(pot),
        str(elix),
        str(gold),
        str(x),
        str(y),
        str(key)
    ]
    
    f = open('load.txt', 'w')
    
    for item in player_list:
        f.write(item + '\n')
    f.close()
def clear():
    os.system('cls')
def stats():
    print(f"{name} Stats: HP:{hp} ATK:{atk} POTIONS:{pot} ELIXERS:{elix} GOLD:{gold}")
def draw():
    print("xX--------------------------------Xx")
def heal(amount):
    global hp
    if hp + amount < hpmax:
        hp += amount
    else:
        hp = hpmax
    print(f"{name}'s HP Refilled to {hp}!")   
def battle():
    global fight, play , run , hp, pot , elix, gold, boss
    
    if not boss:
        enemy = random.choice(e_list)
    else:
        enemy = "Dragon"
    ehp = mobs[enemy]["ehp"]
    ehpmax = ehp
    at = mobs[enemy]["at"]
    g = mobs[enemy]["go"]
    
    while fight:
        clear()
        draw()
        print(f"Defeat The {enemy} Enemy!")
        draw()
        print(f"{enemy}'s HP:{ehp}/{ehpmax}")
        print(f"{name}'s HP:{hp}/{hpmax}")
        print(f"POTIONS:{pot}")
        print(f"ELIXERS:{elix}")
        draw()
        print("1 - ATTACK")
        if pot > 0:
            print("2 - USE POTIONS (30HP)")
        if elix > 0:
            print("3 - USE ELIXER (50HP)")
        draw()

        choice = input("> ")
        
        if choice == "1":
            ehp -= atk
            print(f"{name} DEALT {atk} DAMAGE TO THE {enemy}")
            #Counter attack basically
            if ehp > 0:
                hp -= at
                print(f"{enemy} DEALT {at} DAMAGE TO {name}")
            input("> ")
        if choice == "2":
            if pot > 0:
                pot -= 1
                heal(30)
                hp -= atk
                print(f"{enemy} DEALT {atk} DAMAGE TO {name}")
            else:
                print("No Potions Left!")
            input("> ")
        if choice == "3":
            if elix > 0:
                elix -= 1
                heal(50)
                hp -= atk
                print(f"{enemy} DEALT {atk} DAMAGE TO {name}")
            else:
                print("No Elixers Left!")
            input("> ")
        
        if hp <= 0 :
            print(f"{enemy} Defeated {name} ...")
            draw()
            fight = False
            play = False
            run = False
            print("GAME OVER")
            input("> ")
            hp = 1
            
        if ehp <= 0:
            print(f"{name} Defeated the {enemy}!")
            draw()
            fight = False
            gold += g
            print(f"You've found {g} Gold!") 
            if random.randint(0, 100) <= 30:
                pot += 1
                print("You've found a potion!")
            if enemy == "Dragon":
                draw()
                print("Congratulations, The Dragon is dead. You've finished the game!")
                draw()
                boss = False
                play = False
                run = False
            input("> ")
            clear()
def shop():
    global buy, gold, pot, elix, atk
    while buy:
        clear()
        draw()
        print("Welcome to the shop, Traveler!")
        draw()
        print(f"GOLD:{gold}")
        print(f"POTIONS:{pot}")
        print(f"ELIXERS:{elix}")
        print(f"ATK:{atk}")
        draw()
        print("1 - BUY 1 POTION (30HP) 10 GOLD")
        print("2 - BUY 1 ELIXER (50HP) 20 GOLD ")
        print("3 - UPGRADE WEAPON (+2ATK) 30 GOLD")
        print("4 - LEAVE")
        draw()
        choice = input("> ")
        
        if choice == "1":
            if gold > 10:
                pot += 1
                gold -= 10
                print("You bought 1 potion!")
            else:
                print("Not enough gold")
            input("> ")
        if choice == "2":
            if gold > 20:
                elix += 1
                gold -= 20
                print("You bought 1 elixer!")
            else:
                print("Not enough gold")
            input("> ")
        if choice == "3":
            if gold > 30:
                atk += 2
                gold -= 30
                print("Upgraded to a new weapon!")
            else:
                print("Not enough gold")
            input("> ")
        if choice == "4":
            clear()
            draw()
            print("COME BACK SOON!")
            draw()
            input("> ")
            buy = False
def mayor():
    global speak , key
    
    while speak:
        clear()
        draw()
        print("Hello there ... Hero ! , I am the mayor of this town, \nThere is a strong beast roaming the nights and causing terror among the citizens.") 
        draw()
        time.sleep(2)
        if atk < 15:
            print("You need some time to sharpen your skills, Come back when you're ready!")
            key = False

        else:
            print("Your time has come Hero, I will hand you the key to face the almighty foe, Watch yourself!")
            print("(Obtained a strange looking key.)")
            input("> ")
            key = True
        draw()
        print("1 - LEAVE")
        choice = input("> ")
        
        if choice == "1":
            speak = False
def cave():
        global key, boss, fight
        
        while boss:
            clear()
            draw()
            print("Here lies the cave of the Dragon. What will you do?")
            draw()
            if key:
                print("1 - USE KEY")
            print("2 - TURN BACK")
            draw()
            
            choice = input("> ")
            
            if choice == "1":
                if key:
                    fight = True
                    battle()
            elif choice == "2":
                boss = False   
       
          
while run:
    while menu:
        clear()
        draw()
        print("xX--------PLAINS-OF-EIDOLON-------Xx")
        draw()
        print("1, New Game")
        print("2, Load Game")
        print("3, Rules")
        print("4, Quit Game")
        draw()
        if rules:
            print("Hello , I am the creator of this game.")
            print("This is a simple ASCII Game created by Dani :3")
            rules = False
            choice = ""
            input("> ")
        else: 
            choice = input("# ")
        
        
        if choice == "1":
            clear()
            name = input("What's Your name ?: ")
            clear()
            menu = False
            play = True
            
        elif choice == "2":
            try:
                f = open("load.txt","r")
                load_list = f.readlines()
                if len(load_list) == 9:
                    
                    name = load_list[0][:-1]
                    hp = int(load_list[1][:-1])
                    atk = int(load_list[2][:-1])
                    pot = int(load_list[3][:-1])
                    elix = int(load_list[4][:-1])
                    gold = int(load_list[5][:-1])
                    x = int(load_list[6][:-1])
                    y = int(load_list[7][:-1])
                    key = bool(load_list[8][:-1])
                    clear()
                    print("Welcome back, "+ name + "!")
                    input("> ")
                    menu = False
                    play = True
                else:
                    print('Curropted Save File!')
                    input("> ")
            except OSError:
                print("No Loadable file!")
                input("> ")
        elif choice == "3":
            rules = True
            
        elif choice == "4":
            print("Quitting game ...")
            quit()
                     
    while play:
        save()
        clear()
        if not standing:
            if biome[map[y][x]]["e"]:
                if random.randint(0,100) <= 20:
                    fight = True
                    battle()
           
            
        if play:
            draw()
            if y > 0:
                print("1 - NORTH")
            if x < x_len:       
                print("2 - EAST")
            if y < y_len:
                print("3 - SOUTH")
            if x > 0:
                print("4 - WEST")
            if pot > 0:
                print("5 - USE POTION")
            if elix > 0:
                print("6 - USE ELIXER")
            print("9 - DISPLAY STATS")
            print("0 - SAVE AND GO TO THE MAIN MENU")
            draw()
            print("LOCATION: " + biome[map[y][x]]["t"])
            print("COORDS: ",x,y)
            # for place in map:
                # print(place, ) I wanted to print all the locations with an X indicator of the playe.
                # Will work on that soon
            if map[y][x] == "shop" or map[y][x] == "cave" or map[y][x] == "mayor":
                print("7 - ENTER") 
            
            dest = input("# ")
            
            if dest == "0":
                play = False
                menu = True
                save()
            elif dest == "9":
                stats()
                input("# ")    
            elif dest == "1":
                if y > 0:
                    y -= 1
                    standing = False
            elif dest == "2":
                if x < x_len:
                    x += 1
                    standing = False
            elif dest == "3":
                if y < y_len:
                    y += 1
                    standing = False
            elif dest == "4":
                if x > 0:
                    x -= 1
                    standing = False
            elif dest == "5":
                if pot > 0:
                    pot -= 1
                    heal(30)
                if hp == hpmax:
                    print("Maximum HP!")
                    input("> ")
                else:
                    print("No Potions!")
                input("> ")
                standing = True
            elif dest == "6":
                if elix > 0:
                    elix -= 1
                    heal(50)
                elif hp == hpmax:
                    print("Maximum HP!")
                else:
                    print("No Elixers!")
                input("> ")
                standing = True
            elif dest == "7":
                if map[y][x] == "shop":
                    buy = True
                    shop()
                if map[y][x] == "cave":
                    boss = True
                    cave()
                if map[y][x] == "mayor":
                    speak = True
                    mayor()
            else:
                standing = True