# 9-7 管理员：
# 管理员是一种特殊的用户。编写一个名为Admin的类，让它继承你为完成练习9-3或练习9-5而编写的User类。
# 添加一个名为privileges的属性，用于存储一个由字符串（如"canadd post"、"can delete post"、"can ban user"等）组成的列表。
# 编写一个名为show_privileges()的方法，它显示管理员的权限。创建一个Admin实例，并调用这个方法。

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

class Admin(User):
    def __init__(self,first_name,last_name,*privileges):
        super().__init__(first_name,last_name)
        self.privileges=privileges
    def show_privieges(self):
        print(self.last_name+" "+self.first_name+" is an Admin")
        for i in self.privileges:
            print(i)

admin=Admin("vardy","Jaymi","can add post","can delete post","can ban user")
print(admin.info)
admin.show_privieges()

