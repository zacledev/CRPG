class MaterialData:
    def __init__(self, id, name, density, custom_key : dict = None):
        self.id = id
        self.name = name
        self.density = density
        self.custom_key = custom_key
    def getWeightByDensity(self, density):
        return self.density * density



wood = MaterialData("wood", "Wood", 0.5, {"hardness" : 1, "damage_mult" : 0.4})
iron = MaterialData("iron", "Iron", 7, {"hardness" : 10, "damage_mult" : 1})


material_dic = {"wood" : wood}
