class Person:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def say(self):
        return "我叫" + self.name +"；今年" +str(self.age)+ "岁了;性别是：" + self.sex