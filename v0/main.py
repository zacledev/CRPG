"""
rpg jouable dans la console
on incarnera Seyte, un mec qui vient de mourir
il se reveille au millieu d'une gigantesque plaine.

En réalité il a été téléporté dans un autre monde, un monde créé de toute pièce par le dieu de ce monde.
Il en a marre de la vie et a décidé de se réincarner, puis mourir, c'est le seul moyen pour un dieu de mourir.
Mais pour ça il est obligé de trouver un sucsesseur, il a donc créer cette tour pour récupérer les ames qui lui semblaient avoir un minimum de potentiel pour gravir cette tour.
Le dieu suit avec passion les aventures des gens qu'il emmène dans la tour, car c'est un peu un sadique
sauf qu'il y'a plusieurs dieu, on connait pas leur nombre mais on sait qu'il y'en a plus d'un dizaine, et c'est pas genre "dieu de la création" , "dieu de la guerre" ou quoi, nan c'est tous des dieu au meme pouvoir qui se coltinent l'univers ensemble
le dieu qui cherche un successeur est sadique sa mère, mais un autre l'empeche de trop faire n'importe quoi. Un autre, sera présent durant l'intégralité de votre aventure pour vous aider, sauf quand le "regard de Xeus" sera sur nous. (Xeus est le nom du dieu sadique)
c'est "le roi des dieu" , le plus vieux, l'ancien s'est barré y'a pas longtemps donc il s'est mangé le role de chef, et se fait beaucoup plus surveiller par les autre, il en a donc eu marre

notre personnage sera au millieu d'une tour gigantesque de 10 étage, Lorsqu'on en gravit un, on ne peut plus redescendre. Sauf via l'abysse
Les étages seront immenses, quelques heure de jeu chacun a terminer
On pourra avoir dés le premier étage des armes qui égalent la puissance moyenne du 5eme, sauf que pour ça il faut savoir exactement comment les avoir. T'a autant de chance d'en avoir une sans faire exprès que de terminer outer wild du premier coup les yeux bandés
l'abysse supprime l'intégralité de notre inventaire, on ne garde que notre experience du jeu (comme un rogue like, on garde que ce qu'on a appris sur le jeu)
ah oui, parce que ça me fait rire, l'épée de base qu'on a , et qu'on jette dés qu'on en a une meilleur. Sa sera la clé pour vaincre Xeus. Pourquoi ? parce qu'elle est incassable ! Et que quand on frappe Xeus, toutes nos armes se cassent instantenement, il est un peu comme un objet non défini, tout ce qui le touche disparait.


A un moment, Xeus se rendra compte qu'il y'a quelqu'un qui controle Seyte, et appréciera pas ça des masse. Donc si on profite trop de l'abysse pour revenir, il captera qu'on sait des truc qu'on devrait pas savoir, et comprendra qu'il y'a quelqu'un d'autre derriere
A un moment il sera convaincu que c'est le dieu qui nous aide qui est derrière ça, et le butera, sa se passera en général vers les derniers étage, au dernier si on est vraiment bon.
On pourra aussi parfois parler avec lui, les conversations seront extremement importante, a la fin il nous fera signer des pactes sans nous demander au seul fait de ce qu'on a dit.

Y'aura aussi un culte du sain papier (PaperCult). Sa me fait rire

10 hp seront ceux d'un humain lambda.

le premier ennemi du jeu sera un mec de la secte du papier, sauf qu'on aura une épée en bois, donc va littéralement falloir le tabasser a mort pour le battre

poids : demande des points de forces , reduit la vitesse d'attaque mais augmente les dégats
dégats : si quelqu'un a vraiment besoin de lire cette ligne pour comprendre ce que les dégat font, c'est qu'elle est soit conne, soit moi parce que j'ai oublié que annerie j'ai du mettre
durabilité : si la garde est pas assez solide, en tapant contre un truc dur, il peut se cassé et se séparer du manche. Pas que le manche dailleurs, sa marche pour tout


le joueur aura plein de stat :
vie pour chaque parti du corps, agilité de chaque parti du corps, par exemple pour manier une épée avec un mauvais centre d'équilibre il faudra beaucoup de stat dans le bras et la main. Force par parti du corps, différent de l'agilité.

"""
from v0.data.itemData import *
from v0.data.materialData import *
from v0.data.mobData import *



def getWeightItem(item):
    total_weight = 0
    for part_name, part in item.custom_key.get("weapon_parts", {}).items():
        volume = SHAPE_DATA[part_name][part["shape_type"]]["volume"]
        material = material_dic[part["material"]]
        total_weight += volume * material.getWeightByDensity(volume)
    return total_weight



def fighting_system():
    playerHP = 10
    turn = 0
    player_turn = True
    player_damage = 1
    is_player_blocking = False
    is_player_dodging = False
    while any(e.custom_key["HP"] > 0 for e in enemy_list):
        if player_turn:
            action = input(" (A) Attack, (B) Block, (D) dodge >>> ")
            if action == "A":
                attack = input("You can : (1) Beat the ass of the enemy, (2) Beat the ass of enemy, but with more strenght >>>")
                target = int(input("You can only beat the ass up of one enemy for the moment : 1 >>>")) - 1

                item = item_dic["starter_sword"]
                damage = getWeightItem(item) * material_dic[item.custom_key["weapon_parts"]["blade"]["material"]].custom_key["damage_mult"]


                if attack == "1":
                    enemy_list[target].takeDamage(damage)
                    print(f"{enemy_list[target].name} lost {damage} HP")
                if attack == "2":
                    damage *= 2
                    enemy_list[target].takeDamage(damage)
                    print(f"{enemy_list[target].name} lost {damage} HP")
                player_turn = False
            if action == "B":
                 is_player_blocking = True
            if action == "D":
                is_player_dodging = True
        else:
            for enemy in enemy_list:
                mob_damage = enemy.custom_key["damage"]
                if is_player_blocking:
                    mob_damage /= 2
                    print(f"you blocked, {enemy.name} made you {mob_damage} damage")

                if is_player_dodging:
                    mob_damage = 0
                    print(f"You dodge ! {enemy.name} made you absolutely no damage")
                else:
                    print(f"{enemy.name} made you {mob_damage} damage")
                playerHP -= mob_damage
            player_turn = True


while True:
    action = input("Hi onni chan, what you wanna do :3 >>> ")
    print("Nah i don't care, join the PaperCult instead")
    print(tutorial_paper.read())
    verb, args = action.split()[0], action.split()[1:]
    if verb == "desc":
        item = item_dic[args[0]]
        item.desc()
        print(getWeightItem(item))
    if verb == "fight":
        fighting_system()
