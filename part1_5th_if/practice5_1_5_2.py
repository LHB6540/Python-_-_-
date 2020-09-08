# 编写一系列条件测试；将每个测试以及你对其结果的预测和实际结果都打印出来
# 对于下面列出的各种测试，至少编写一个结果为True和False的测试。
# ·检查两个字符串相等和不等。
# ·使用函数lower()的测试。
# ·检查两个数字相等、不等、大于、小于、大于等于和小于等于。
# ·使用关键字and和or的测试。·测试特定的值是否包含在列表中。
# ·测试特定的值是否未包含在列表中。
car1 = 'audi'
car2 = 'toyota'
car3 = 'audi'
car4 = 'Audi'

print('Is car1==car2,I guess False')
print(car1 == car2)

print("\nIs car1==car3,I guess True")
print(car1 == car3)

#下列省略猜测输出语句，仅注释并输出结果

#True
print(car1 == car4.lower())

#False
print(2 == 3)

#True
print(2 < 3)

#False
print(2 >= 3)

#True
print(2 <= 3)

#False
print(car1 == car2 and car1 == car3)

#True
print(car1 == car2 or car1 == car3)

#False
cars = ['audi', 'toyota', 'bmw']
print('suzuki' in cars)

#True
print('suzuki' not in cars)