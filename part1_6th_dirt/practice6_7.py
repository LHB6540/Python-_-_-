# 6-7 人：
# 在为完成练习6-1而编写的程序中，再创建两个表示人的字典，然后将这三个字典都存储在一个名为people的列表中。
# 遍历这个列表，将其中每个人的所有信息都打印出来。

people_info = {
    'first_name': 'David',
    'last_name': 'Beckham',
    'city':'London'
    }
people_info_1 = {
    'first_name': 'Allen',
    'last_name': 'Walker',
    'city':'NewYork'
    }
people_info_2 = {
    'first_name': 'Jim',
    'last_name': 'Vardy',
    'city':'London'
    }
people_info_list = [people_info, people_info_1, people_info_2]
for i in people_info_list:
    for key, value in i.items():
        print(key + ':' + value)
    print('\n')