# 10-5 关于编程的调查：
# 编写一个while循环，询问用户为何喜欢编程。每当用户输入一个原因后，都将其添加到一个存储所有原因的文件中。
file_name='reason_for_program'
with open(file_name,'a') as file_project:
    while True:
        name=input("Please input your name,input exit to stop this program:")
        if name=='exit':
            break
        reason=input("Please input your reason for programming,input exit to stop this program")
        if reason=='exit':
            break
        file_project.write(name+':'+reason+"\n")

with open(file_name) as  file_project:
    print(file_project.read())