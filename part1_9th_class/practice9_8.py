# 9-8 权限：编写一个名为Privileges的类，它只有一个属性——privileges，其中存储了练习9-7所说的字符串列表。
# 将方法show_privileges()移到这个类中。在Admin类中，将一个Privileges实例用作其属性。
# 创建一个Admin实例，并使用方法show_privileges()来显示其权限。

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

class Privileges():
    def __init__(self,*privileges):
        self.privileges=privileges
    def show_privileges(self):
        for i in self.privileges:
            print(i)

class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.Privileges=Privileges()
admin=Admin("Vardy","Jaymi")
admin.Privileges.privileges=("can add post","can delete post","can ban user")
admin.Privileges.show_privileges()

