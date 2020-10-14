# 10-3 访客：编写一个程序，提示用户输入其名字；用户作出响应后，将其名字写入到文件guest.txt中。
with open('guest.txt','a') as  file_object:
    while True:
        name=input("please in put your name,input exit to stop this program:")
        if name=='exit':
            break
        else:
            file_object.write(name+"\n")

with open('guest.txt') as file_object:
    print(file_object.read())