# 10-9 沉默的猫和狗：
# 修改你在练习10-8中编写的except代码块，让程序在文件不存在时一言不发。

try:
    with open('cats.txt') as file_object:
        print(file_object.read())
except FileNotFoundError:
    pass


try:
    with open('../dogs.txt') as file_object:
        print(file_object.read())
except FileNotFoundError:
    pass

