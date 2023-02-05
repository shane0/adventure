class Player:
    # count = 0

    def __init__(self, name, hp):
        # Player.count += 1
        self.name = name
        self.hp = hp
        self.items = []
        self.abilities = []

    def add_item(self, item):
        self.items.append(item)

    def add_ability(self, ability):
        self.abilities.append(ability)

    def move_hunger(self):
        """moving causes damage"""
        self.hp -= 1
        bar = {
            0: "",
            1: "=",
            2: "==",
            3: "===",
            4: "====",
            5: "=====",
            6: "======",
            7: "=======",
            8: "========",
            9: "=========",
            10: "==========",
            11: "===========",
            12: "============",
            13: "=============",
            14: "==============",
            15: "================",
        }
        print("HP: ", self.hp, bar[self.hp])
