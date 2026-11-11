
class MobData:
    def __init__(self, id, name, custom_key : dict):
        self.id = id
        self.name = name
        self.custom_key = custom_key


class Mob:
    def __init__(self, data):
        self.id = data.id
        self.name = data.name
        self.custom_key = data.custom_key
    def takeDamage(self, damage):
        self.custom_key["HP"] -= damage








paperCultBasicMember = MobData("paperCultBasicMember", "Paper Cult Basic Member", {"damage" : 1, "HP" : 9, "Intelligence" : 0})
paperCultBasicMember1 = Mob(paperCultBasicMember)

enemy_list = [paperCultBasicMember1]

