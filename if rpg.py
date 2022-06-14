import random

#hp for characters
player_health = 100
monster1_health = 20
monster2_health = 50
boss_health = 300

# attack powers
player_attack = 20
monster1_attack = 10
monster2_attack = 20
boss_attack = 35

#enemy names
monster1_name = "Slime"
monster2_name = "Wolf"
boss_name = "Krupa"

# functions
def AttackPlayer():
    global player_health
    attacking_enemy = random.randint(0,2)
    print(attacking_enemy)

    # deal damage to the player
    if attacking_enemy == 0:
        # slime attacks the player
        player_health = player_health - monster1_attack
        print(player_health)
    if attacking_enemy == 1:
        # wolf attacks the player
        player_health = player_health - monster2_attack
        print(player_health)
    if attacking_enemy == 2:
        # boss attacks the player
        player_health = player_health - boss_attack
        print(player_health)


def AttackEnemy():
    global monster1_health
    global monster2_health
    global boss_health
    who_to_attack = input("Who will you attack? \n")

    if who_to_attack == monster1_name:
        #deal damage to slime
        monster1_health = monster1_health - player_attack
        print(monster1_health)

    if who_to_attack == monster2_name:
        #deal damage to wolf
        monster2_health = monster2_health - player_attack
        print(monster2_health)

    if who_to_attack == boss_name:
        #deal damage to Krupa
        boss_health = boss_health - player_attack
        print(boss_health)

while player_health > 0 and monster1_health > 0 \
      and monster2_health > 0 and boss_health > 0:
    
    AttackEnemy()

    # now, the enemies attack the player
    # pick one random enemy

    AttackPlayer()

    
# check if the player is alive

# check if the enemies are alive

