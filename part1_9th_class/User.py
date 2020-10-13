class User1():
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
