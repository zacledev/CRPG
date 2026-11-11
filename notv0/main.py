class Item_data:
    def __init__(self, id, name, description, damage):
        self.id = id
        self.name = name
        self.description = description
        self.damage = damage
        

class Mob_data:
    def __init__(self, id, name, max_hp, damage, surprise_attack_cooldown):
        self.id = id
        self.name = name
        self.max_hp = max_hp
        self.damage = damage
        self.surprise_attack_cooldown = surprise_attack_cooldown


class Mob:
    next_id = 1
    def __init__(self,Mob_data):
        self.id = Mob.next_id
        Mob.next_id += 1

        self.type_id = Mob_data.id
        self.name = Mob_data.name
        self.max_hp = Mob_data.max_hp
        self.hp = Mob_data.max_hp
        self.damage = Mob_data.damage
        self.surprise_attack_cooldown = Mob_data.surprise_attack_cooldown
    def die(self):
        pass
    def take_damage(self, damage):
        self.hp -= damage
        print(f"{self.name}.{self.id} perd {damage} HP !")
        print(f"{self.name}.{self.id} a maintenant {self.hp}/{self.max_hp} !")


        if self.hp <= 0:
            print(f"{self.name}.{self.id} est mort ! ")
            self.die()


    def show_stats(self):
        print(f"identifiant du mob : {self.id} \n",
              f"nom du mob : {self.name} \n",
              f"vie du mob : {self.hp}/{self.max_hp} \n",
              f"dégat du mob : {self.damage}",
              )


"""en gros le systeme d'attaque va marcher en "temps reel" : 
chaque attaque aura un temps d'execution, un temps pour la commencer, le moment ou sa touche l'ennemi, 
et le moment ou tu peut refaire une attaque, et peut être meme la position avec laquel tu fini, 
donc en fonction tu pourra enchainer d'autre attaque plus ou moins rapidement

imaginons, on commence le combat face a un goblin, on immagine que comme on le prend par surprise on a 0,5sec avant qu'il commence a attaquer
Je lance "Attaque Epee basique" , qui dure 1.2 sec, et qui touche l'ennemi a 0.7 sec.
Le goblin réagit au bout de 0.5 sec, et lance une esquive qui dure au total 2 sec et qui bloque tout les coups entre 1.2 et 1.8 sec. 
Un mob plus intelligent aurait lancé un blocage ou un autre truc car il aurait su pertinnement qu'il allait rater son esquive
L'attaque touche donc le goblin, le joueur peut rejouer, le goblin lui, a encore 1.8 sec "d'animation"
Et ainsi de suite


"""

def attack_player(damage):
    print(f"le player a été attaqué de {damage}")

def attack(target_mob, attack_type, item):
    if attack_type == "basic":
        target_mob.take_damage(item.damage)

mob_list = {}

def attack_system(enemy : list, surprise_attack = False):
    #time is in frame
    frame = 10
    time = 0
    time_line = {}
    for i in range(0, 100):
        time_line[i] = None
    player_cooldown = 0
    mob_cooldown = []

    if surprise_attack:
        for i in range(0, len(mob_cooldown)):
            mob_cooldown[i] = enemy[i].surprise_attack_cooldown
    else:
        for i in range(0, len(mob_cooldown)):
            mob_cooldown[i] = 0
    print(mob_cooldown)

    while True:
        time += 1
        player_cooldown -= 1
        for i in range(0, len(mob_cooldown)):
            mob_cooldown[i] -= time
        for i in range(0, len(mob_cooldown)):
            if mob_cooldown <= 0:
                time_line[7].append(attack_player) #valeur arbitraire
        for i in range(1, 100):
            time_line[i] = time_line[i + 1]
        time_line[0](10)


def spawn_mob(Mob_data):
    m = Mob(Mob_data)
    mob_list[m.id] = m
    return m

def choose_item():
    item = input("Epee (1) ou Hache (2) ? >>> ")
    if item == "1":
        print("Vous avez choisi l'Epee")
        return sword
    elif item == "2":
        print("Vous avez choisi la Hache")
        return axe

sword = Item_data("sword", "Sword", "A basic sword who can do everything you should expect from a basic sword", 5)
axe = Item_data("axe", "Axe", "A basic axe who can do everything you should expect from a basic axe", 8)
zombie = Mob_data("zombie", "Zombie", 20, 2, 0.5)

zombie01 = spawn_mob(zombie)
zombie02 = spawn_mob(zombie)

item = choose_item()
attack(zombie01, "basic", item)
item = choose_item()
attack(zombie02, "basic", item)
zombie01.show_stats()
zombie02.show_stats()