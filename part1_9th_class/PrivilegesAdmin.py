import User
class Privileges():
    def __init__(self,*privileges):
        self.privileges=privileges
    def show_privileges(self):
        for i in self.privileges:
            print(i)

class Admin(User.User1):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.Privileges=Privileges('add','post')