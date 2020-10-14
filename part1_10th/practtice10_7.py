# 10-7 加法计算器：
# 将你为完成练习10-6而编写的代码放在一个while循环中，让用户犯错（输入的是文本而不是数字）后能够继续输入数字。
num1=0
num2=0
while True:
    try:
        num1=input("Please input a number:")
        num1=float(num1)
    except:
        print("Please input again")
    else:
        break
while True:
    try:
        num2=input("Please input another number")
        num2=float(num2)
    except:
        print("Plese input again")
    else:
        break

print(num2+num1)


