#coding:utf-8

class Role(object):
    def __init__(self,name,role,weapon,life_value):
        self.name=name
        self.role=role
        self.weapon=weapon
        self.life_value=life_value

    def buy_weapon(self,weapon):
        print("%s is buying %s" %(self.name,weapon))
        self.weapon=weapon

p1=Role("billy","police","B11",100)  #等同于Role(p1,"billy","police","B11",100)
#p1叫Role的实例
#把一个抽象的类变成一个具体对象的过程叫实例化

p1.buy_weapon("AK47")
print (p1.weapon)


