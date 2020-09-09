# 6-10 喜欢的数字：
# 修改为完成练习6-2而编写的程序，让每个人都可以有多个喜欢的数字，然后将每个人的名字及其喜欢的数字打印出来。
favorite_number = {'Li': [16, 6, 1], 'zhang': [1, 2, 3], 'wang': [2, 3, 4], 'zhu': [3, 4, 5], 'bai': [4, 5, 6]}

for key, value in favorite_number.items():
    print(key + '\'s favorite number are:')
    for num in value:
        print(num)