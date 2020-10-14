# 10-8 猫和狗：
# 创建两个文件cats.txt和dogs.txt，在第一个文件中至少存储三只猫的名字，在第二个文件中至少存储三条狗的名字。
# 编写一个程序，尝试读取这些文件，并将其内容打印到屏幕上。
# 将这些代码放在一个try-except代码块中，以便在文件不存在时捕获FileNotFound错误，并打印一条友好的消息。
# 将其中一个文件移到另一个地方，并确认except代码块中的代码将正确地执行。

try:
    with open('cats.txt') as file_object:
        print(file_object.read())
except FileNotFoundError:
    print('the file does not exist')



try:
    with open('../dogs.txt') as file_object:
        print(file_object.read())
except FileNotFoundError:
    print('the file does not exist')
