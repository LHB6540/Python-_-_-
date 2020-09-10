# 函数
def greet():
    '''函数文档'''
    print('Hello')
greet()

def greet(username):
    '''带参数'''
    print('hello '+ username)
greet('wang')

# 传递实参的方式
# 位置
def describe_pet(pet_type,pet_name):
    '''显示宠物信息'''
    print('My ' + pet_type + ' name is ' + pet_name)
describe_pet('cat','mimi')

# 关键字
describe_pet(pet_type='dog',pet_name='wangwang')

# 默认值,默认值位置在后
def describe_pet1(pet_name,pet_type='dog'):
    '''显示宠物信息'''
    print('My ' + pet_type + ' name is ' + pet_name)
describe_pet1('wangwang')
describe_pet1('wangwang','dog')

# 实参可选，将形参默认值设为空字符串，函数内分支

# 返回值
def get_full_name(first_name,last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
print(get_full_name('david','beckham'))

# 可返回字典、列表等

# 传递列表，修改列表
# 禁止修改列表，使用切片传递副本

# 未知参数，将参数封装进一个名称前带*的元组中
# 已知参数在前，位置参数在后
# 任意数量的关键字参数，前加**，传递实参时，视为封装的字典

# 导入模块引用函数 import module      module.function()
# 导入特定函数 from module import function
# 导入所有函数 from module import *
# 使用as将导入的函数重命名 from module import function as other_name
# 使用as将模块重命名 import module as other_name
