# 9-5 尝试登录次数：
# 在为完成练习9-3而编写的User类中，添加一个名为login_attempts的属性。
# 编写一个名为increment_login_attempts()的方法，它将属性login_attempts的值加1。
# 再编写一个名为reset_login_attempts()的方法，它将属性login_attempts的值重置为0。
# 根据User类创建一个实例，再调用方法increment_login_attempts()多次。
# 打印属性login_attempts的值，确认它被正确地递增；
# 然后，调用方法reset_login_attempts()，并再次打印属性login_attempts的值，确认它被重置为0。

class User():
    def __init__(self,first_name,last_name,*info):
        self.first_name=first_name
        self.last_name=last_name
        self.info=info
        self.login_attempts=0
    def describe_user(self):
        print(self.last_name+" "+self.first_name+" has these info:")
        for i in self.info:
            print(i)
    def greet_user(self):
        print("Hi,"+self.last_name+" "+self.first_name)
    def increment_login_attempts(self):
        self.login_attempts+=1
    def reset_login_attempts(self):
        self.login_attempts=0

user=User("Vardy","Jim")
for i in range(1,9):
    user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)