magicians = ["alice","david","carolina"]
for magician in magicians:
    print(magician.title()+",that was a great trick")
    print("I can't wait to your next trick," + magician.title() + ".\n")
print("Thank you,everyone.That was a great magic show!")

for value in range(1, 5):
    print(value)
#make range to list
numbers = list(range(1, 6))
print(numbers)
#the step of range
even_numbers = list(range(2, 12, 2))
print(even_numbers)

squars = []
for value in range(1, 11):
    squars.append(value ** 2)
print(squars)

# 处理数字列表的函数
digits = list(range(2, 78))
print(min(digits))
print(max(digits))
print(sum(digits))

# 列表解析
numbers_list = [value ** 2 for value in range(1, 11)]
print(numbers_list)


# 切片，起始于起始索引，结束于结束索引前一位
palyers = ['charles', 'martina', 'michael', 'florence', 'eli']
# 第一个至第三个
print(palyers[0:3])
# 第二个至第四个
print(palyers[1:4])
# 省略起始元素,开始于列表开头
print(palyers[:4])
# 省略结束元素，结束于末尾
print(palyers[2:])
# 使用负数索引
# 使用负数索引时，由于最后一个元素为-1，如果加0表示范围则会发生冲突，因此省略表示
print(palyers[-3:])

# 复制列表
copy_players = palyers[:]
# 直接等于变量名是添加引用

# 元组
dimensions = (0, 1, 2)
# 不能更改元组内的值，但可以更改元组变量
dimensions=(0,1,2,3)
