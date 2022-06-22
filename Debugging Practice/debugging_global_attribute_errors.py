character_name = "Cloud"
character_hp = 100
character_mp = 50

def update_hp(delta):
    character_hp = character_hp + delta



enemy_attack_damage = 10

update_hp(-enemy_attack_damage)

print(character_hp)

def update_mp(mp, delta):
    mp = mp + delta

update_mp(character_mp, 10)

print(character_mp)


print(character_name.conjugate())
print(character_hp.append(character_name))
