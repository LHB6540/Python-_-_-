# 10-11 喜欢的数字：
# 编写一个程序，提示用户输入他喜欢的数字，并使用json.dump()将这个数字存储到文件中。
# 再编写一个程序，从文件中读取这个值，并打印消息“I know your favoritenumber! It's _____.”。
import json

name=input("Please input your favorite number:\n")
file_num='number.txt'
with open(file_num,'w') as js_file:
    json.dump(name,js_file)

with open(file_num) as js_file:
    num=json.load(js_file)
print("I know your favoritenumber!It's "+num)
