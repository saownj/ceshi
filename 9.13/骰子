class Die:
    def __init__(self, sides=6, sun_1=1):
        self.sides = int(sides)
        self.sun_1 = int(sun_1)
    def roll_die(self):
        list_1= []
        while True:
            for i in range(1, self.sun_1 + 1) :
                roll = randint(1, self.sides)
                list_1.append(roll)
                if i == self.sun_1:
                    return list_1
die= Die(int(input("每个骰子的点数")),int(input("共有几个骰子")))
print(f"{die.roll_die()}")
