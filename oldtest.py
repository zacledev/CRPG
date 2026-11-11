from dataclasses import dataclass
from functools import partial
from random import *


@dataclass(frozen=True)
class Attack:
    id: str
    name: str
    desc: str
    min_damage: int
    max_damage: int
    hit_delay: int
    duration : int

class Item_data:
    def __init__(self, id, name, description, Attack_list):
        self.id = id
        self.name = name
        self.description = description
        self.Attack_list = Attack_list



@dataclass(frozen=True)
class Mob_data:
    id: str
    name: str
    max_hp: int
    damage : int
    surprise_attack_cooldown: int  # En frames, comme tous les timings.
    hit_delay: int


class Mob:
    next_id = 1

    def __init__(self, Mob_data):
        self.id = Mob.next_id
        Mob.next_id += 1

        self.type_id = Mob_data.id
        self.name = Mob_data.name
        self.max_hp = Mob_data.max_hp
        self.hp = Mob_data.max_hp
        self.damage = Mob_data.damage
        self.surprise_attack_cooldown = Mob_data.surprise_attack_cooldown
        self.hit_delay = Mob_data.hit_delay

    def die(self):
        mob_list.pop(self.id, None)

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

def attack(atk, target):
    if target.hp <= 0:
        return
    damage = randint(atk.min_damage, atk.max_damage)
    target.take_damage(damage)

def choose_enemy():
    alive = [m for m in mob_list.values() if m.hp > 0]
    for i, m in enumerate(alive, 1):
        print(f"({i}) {m.name}.{m.id} {m.hp}/{m.max_hp}")
    while True:
        choice = input("Attaque un ennemi >>> ")
        return alive[int(choice) - 1]

def choose_item():
    print("Vous avez choisi l'Epee")
    return sword


def choose_attack(item):
    for i, a in enumerate(item.Attack_list, 1):
        print(f"({i}) {a.name}")
    choice = int(input("Quel attaque faire ? >>> "))
    return item.Attack_list[int(choice) - 1]


def attack_system(enemy: list, surprise_attack=False):
    max_frame = 30
    time = 0
    time_line = {}
    for i in range(0, max_frame):
        time_line[i] = []
    player_cooldown = 0

    if surprise_attack:
        mob_cooldown = [e.surprise_attack_cooldown for e in enemy]
    else:
        mob_cooldown = [0] * len(enemy)
    print(mob_cooldown)

    while time < 100 and any(e.hp > 0 for e in enemy):
        time += 1
        player_cooldown -= 1
        for i in range(0, len(mob_cooldown)):
            mob_cooldown[i] -= 1
        for i in range(0, len(mob_cooldown)):
            if mob_cooldown[i] <= 0 and enemy[i].hp > 0:
                time_line[enemy[i].hit_delay].append(partial(attack_player, enemy[i].damage))
                mob_cooldown[i] = 15
        if player_cooldown <= 0:
            item = choose_item()
            atk = choose_attack(item)
            target = choose_enemy()
            time_line[atk.hit_delay].append(partial(attack, atk, target))
            player_cooldown = atk.duration
        # print(time_line)

        for action in time_line[0]:

            print(f"[{time}] ", end = "")
            action()

        for i in range(0, max_frame - 1):
            time_line[i] = time_line[i + 1]
        time_line[max_frame - 1] = []


def spawn_mob(Mob_data):
    m = Mob(Mob_data)
    mob_list[m.id] = m
    return m


mob_list = {}

Attack_list = []
Attack_list.append(Attack("basic_attack", "Basic Attack", "The most common attack you could possibly imagine", 3, 5, 2, 5))
Attack_list.append(Attack("critical_attack", "Critical Attack", "A commun attack, but more powerfull", 9, 13, 6, 15))

sword = Item_data("sword", "Sword", "A basic sword who can do everything you should expect from a basic sword", Attack_list)
 # axe = Item_data("axe", "Axe", "A basic axe who can do everything you should expect from a basic axe", )
goblin = Mob_data("goblin", "Goblin", 20, 2, 5, 7)

goblin01 = spawn_mob(goblin)
goblin02 = spawn_mob(goblin)
enemy = [goblin01, goblin02]
attack_system(enemy, True)

"""
basic attack : 3-5 dégat, un ennemi touché. 5 , touche l'ennemi 2 frame , 
critical attack : 9 - 13, un ennemi touché, 15 , touche l'ennemi a 6 frame, 30 frame de cooldown (pr cette attaque précisement)
swing attack : 2 - 3, jusqu'a 3 ennemi touché, 12, touche l'ennemi a frame 2, 4 et 6, le temps d'animation dimunue de 2 pour chaque ennemi en moins
dodge : esquive l'attaque, 13 frame d'animation, dodge entre frame 3 et 10
block : bloque l'attaque, 5 frame d'animation, bloque l'attaque entre la frame 2 et 4. Reduit les dégat subi de 50%

attaque des goblin
basic attack : 1 - 2 dégat, cible unique, 6 frame, touche l'ennemi a 2 frame
dodge : esquive l'attaque, 10 frame d'animation, dodge entre 3 et 8


"""

"""
item = choose_item()
attack(zombie01, "basic", item)
item = choose_item()
attack(zombie02, "basic", item)
zombie01.show_stats()
zombie02.show_stats()"""