class ItemData:
    def __init__(self, id, name, description, custom_key : dict):
        self.id = id
        self.name = name
        self.description = description
        self.custom_key = custom_key
    def read(self):
        if self.custom_key["is_readable"]:
            return self.custom_key["text"]
    def desc(self):
        print(self.id)
        print(self.name)
        print(self.description)
    def get_damage(self):
        min_damage = 0
        max_damage = 0


starter_sword = ItemData(
    "starter_sword", "Starter Sword", "Wtf ? are you really reading ts ?? WDF DO YOU EXPECT A SWORD THIS BASIC TO DO",
    {"weapon_type" : "basic_sword",
    "weapon_parts" : {
        "blade"  : {
            "shape_type" : "basic",
            "material" : "wood"
        },
        "guard"  : {
            "shape_type" : "basic",
            "material" : "wood"
        },
        "handle" : {
            "shape_type" : "basic",
            "material" : "wood"
        }
    },
    "durability" : -1})
iron_sword = ItemData(
    "iron_sword", "Iron Sword", "Ts is like the previous sword but heavier, it's not that hard",
    {"weapon_type": "basic_sword",
     "weapon_parts": {
         "blade": {
             "shape_type": "basic",
             "material": "iron"
         },
         "guard": {
             "shape_type": "basic",
             "material": "wood"
         },
         "handle": {
             "shape_type": "basic",
             "material": "wood"
         }
     },
     "durability": 100})
tutorial_paper = ItemData("tutorial_paper", "THE tutorial paper",
                          "For the blind, it is vision. For the hungry, it is the chef. For the deaf, it is the sound (maybe not). For the thirsty, it is water (i'm pretty shure it's paper...). If Paper thinks, YOU agree. If Paper speaks (how the fuck it would talk), I'm listening. If Paper has a million fans, You are one of them... If Paper has only one fan, You are the only fan (I hope i don't have copyright issue with this one)... If Paper has no fans, You no longer exist. If the whole world is against Paper, You are against the whole world",
                          {"is_readable" : True, "text" : "For the blind, it is vision. For the hungry, it is the chef. For the deaf, it is the sound (maybe not). For the thirsty, it is water (i'm pretty shure it's paper...). If Paper thinks, YOU agree. If Paper speaks (how the fuck it would talk), I'm listening. If Paper has a million fans, You are one of them... If Paper has only one fan, You are the only fan (I hope i don't have copyright issue with this one)... If Paper has no fans, You no longer exist. If the whole world is against Paper, You are against the whole world"})



SHAPE_DATA = {
    "blade" : {
        "basic" : {
            "volume" : 1,
            "durability" : 100
        }
    },
    "guard" : {
        "basic" :  {
            "volume" : 0.03,
            "durability" : 100
        }
    },
    "handle" : {
        "basic" :  {
            "volume" : 0.075,
            "durability" : 100
        }
    }
}

item_dic = {"starter_sword":  starter_sword, "tutorial_paper": tutorial_paper}

