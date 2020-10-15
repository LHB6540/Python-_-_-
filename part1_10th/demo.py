# 一次读取
with open('pi_digits.txt') as file_object:
    content=file_object.read()
    print(content.rstrip())

# 逐行读取
file_name='pi_digits.txt'
with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())

# 行列表
with open(file_name) as  file_object:
    lines=file_object.readlines()
for line in  lines:
    print(line.rstrip())

# 写入文件,w先清空再写入
with open('programming.txt','r+') as file_object:
    file_object.write("I love this program")
with open('programming.txt') as file_object:
    print(file_object.read())
# 注意多行添加换行符
with open('programming1.txt','w') as file_object:
    file_object.write("I love this program\n")
    file_object.write("I love program\n")
with open('programming1.txt') as  file_object:
    print(file_object.read().rstrip())
# 附加写入
with open('programming1.txt','a') as file_object:
    file_object.write("Me，too")
with open('programming1.txt') as file_object:
    print(file_object.read())




