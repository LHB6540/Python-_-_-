# 10-13 验证用户：
# 最后一个remember_me.py版本假设用户要么已输入其用户名，要么是首次运行该程序。
# 我们应修改这个程序，以应对这样的情形：当前和最后一次运行该程序的用户并非同一个人。
# 为此，在greet_user()中打印欢迎用户回来的消息前，先询问他用户名是否是对的。
# 如果不对，就调用get_new_username()让用户输入正确的用户名。

import json

file_name='remeber_me.json'
def get_stored_name():
    try:
        with open(file_name) as js_file:
            username=json.load(js_file)
    except:
        return None
    else:
        return username

def get_new_name():
    name=input("Please input your name:\n")
    with open(file_name,'w') as js_file:
        json.dump(name,js_file)
    return name

def greet_user():
    user_name=get_stored_name()
    if user_name:
        print("If "+user_name+" is your name?(Y/N)")
        answer=input()
        if answer=='Y':
            print("Welcome back,"+user_name+"!")
        else:
            name=get_new_name()
            print('Welcome back,' + name)
    else:
        name=get_new_name()
        print('Welcome back,'+name)

greet_user()




