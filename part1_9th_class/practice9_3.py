# 9-3 用户：
# 创建一个名为User的类，其中包含属性first_name和last_name，还有用户简介通常会存储的其他几个属性。
# 在类User中定义一个名为describe_user()的方法，它打印用户信息摘要；
# 再定义一个名为greet_user()的方法，它向用户发出个性化的问候。
# 创建多个表示不同用户的实例，并对每个实例都调用上述两个方法。

class User():
    def __init__(self,first_name,last_name,*info):
        self.first_name=first_name
        self.last_name=last_name
        self.info=info
    def describe_user(self):
        print(self.last_name+" "+self.first_name+" has these info:")
        for i in self.info:
            print(i)
    def greet_user(self):
        print("Hi,"+self.last_name+" "+self.first_name)

user1= User("Beckham","David","45","hansome")
user1.describe_user()
user1.greet_user()
user2=User("Vardy","Jam","football player","Best shooter 2019")
user2.describe_user()
user2.greet_user()
