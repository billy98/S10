#_*_coding:utf-8_*_
__author__ = 'alex'
info2 = 'test22'

class People(object):
    info = 'test '

    def __init__(self,name,age,job): #构造函数
        self.name  = name #变成实例变量   等号前面的name和等号后面的name没有关系，前面的name可以取任意名字
        self.__age = age
        self.job = job
        self.info = 't2'
        self.info_dic = {"name": 't1',
                "age":"33"}
        #print '---running __init__'
    def get_info(self,info_type):
        if info_type == 'age':
            return self.__age
        elif info_type == 'job':
            return self.job
    def __breath(self):
        print "%s is breathing..." %self.name
    def walk(self):
        print "I am walking...."
        self.__breath()
        info3 = 't43'
    def talk(self):
        print "talking with sb...",People.info

p1 = People("WangSanJin",29,"BaoAN")
print p1.name ,p1.get_info("age"),p1._People__age
p2 = People("HuangWenShan",22,"BaoMu")
p3 = People("T3",22,"BaoMu")

p1.walk()