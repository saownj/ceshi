from random import choice
import re

class Lottery:
    def __init__(self, list_1, number=4):
        self.list_1= list_1
        self.number= number
    def lottery_1(self):
        print(self.list_1,self.number)
        a = 1
        while a <= self.number:
            list_2.append(choice(self.list_1))
            a += 1
        return list_2

list_1= []
list_2= []
for i in range(0,10):
    list_1.append(i)
    # list_1.append(int(input("输入10个数字")))
for i in range(0,5):
    list_1.append(input("输入5个字母"))

lottery= Lottery(list_1,int(input("输入要抽取几个数字，从列表处")))
print(lottery.lottery_1())
