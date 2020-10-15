# 10-12 记住喜欢的数字：
# 将练习10-11中的两个程序合而为一。
# 如果存储了用户喜欢的数字，就向用户显示它，否则提示用户输入他喜欢的数字并将其存储到文件中。
# 运行这个程序两次，看看它是否像预期的那样工作。

import json
file_name='favorite_num.txt'

def read_num():
    try:
        with open(file_name) as js_file:
            num=json.load(js_file)
            return num
    except:
        return None

def input_num():
    num=input("Please iuput your number:")
    with open(file_name,'w') as  js_file:
        json.dump(num,js_file)

number=read_num()
if number:
    print(number)
else:
    input_num()
    read_num()