# 10-4 访客名单：
# 编写一个while循环，提示用户输入其名字。
# 用户输入其名字后，在屏幕上打印一句问候语，并将一条访问记录添加到文件guest_book.txt中。
# 确保这个文件中的每条记录都独占一行。

with open('guest.txt','a') as file_project:
    while True:
        name=input('Please input your name:')
        if name=='exit':
            break
        print('Hello,'+name)
        file_project.write(name+"\n")

with open('guest.txt') as file_project:
    print(file_project.read())