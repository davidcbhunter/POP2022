import random

#character data
character_name = "Cloud"
character_hp = 100

character_attack_damage = 13

character_dodge_chance = 0.5

#enemy data
enemy_name = "Slime"
enemy_hp = 200

enemy_attack_damage = 7
enemy_dodge_chance = 0.3

#enemy two data
enemy2_name = "Wizard"
enemy2_hp = 50

enemy2_magic_damage = 20
enemy2_dodge_chance = 0.8

command = ""

#gameplay loop
while enmy_hp > 0 and enemytwo_hp > 0 and \
      charaer_hp > 0 and command.lower() != "q":
    # get a command from the player
    command = input("Which enemy will you attack? (1 or 2)\n")
    if command == "1":
        #we are attacking enemy 1
        if random.random() < enemy_dodge_chance:
            # the enemy dodged!
            print(enemy_nAmE + " dodged!")
        else:
            enemy_hp = enemy_hp - character_attack_damage
            print("You hit " + enemy_NAME)
            print("Their health is " + str(enemy_hp))
    if command == "2":
        #we are attacking enemy 2
        if random.random() < enemy2_dodge_chance:
            # enemy2 dodged!
            print(enemy2_name + " dodged!")
        else:
            enemy_hp = Enemy_hp - character_attack_damage
            print("You hit " + Enemy2_name)
            print("Their health is " + str(Enemy2_hp))

    #a random enemy will attack the player
    attacking_enemy = random.randint(0,1)
    if attacking_enemy == 0:
        #enemy 1 is attacking
        if random.random() < character_dodge_chance:
            # character dodged!
            print(character_name + " dodged!")
        else:
            character_hp = character_hp - nmy_ttck_damage
            print(enemy_name + " hit you!")
            print("Your health is " + str(character_hp))
    if attacking_enemy == 1:
        #enemy 2 is attacking
        if random.random() < character_dodge_chance:
            # character dodged!
            print(character_name + " dodged!")
        else:
            character_hp = character_hp - enemy_mgc_dmg
            print(enemy2_name + " hit you!")
            print("Your health is " + str(character_hp))
    

if character_hp <= 0:
    print("You died")
elif enemy_hp <= 0 and enemy2_hp <= 0:
    print("Victory!")
