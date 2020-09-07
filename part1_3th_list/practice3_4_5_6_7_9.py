# 如果你可以邀请任何人一起共进晚餐（无论是在世的还是故去的），你会邀请哪些人？
# 请创建一个列表，其中包含至少3个你想邀请的人；然后，使用这个列表打印消息，邀请这些人来与你共进晚餐。
dinner_friend = ['bai', 'ye', 'xie', 'zhu']
print("Hi,"+dinner_friend[0]+",I want to have a dinner with you")
print("Hi,"+dinner_friend[1]+",I want to have a dinner with you")
print("Hi,"+dinner_friend[2]+",I want to have a dinner with you")
print("Hi,"+dinner_friend[3]+",I want to have a dinner with you")

# 修改嘉宾名单：你刚得知有位嘉宾无法赴约，因此需要另外邀请一位嘉宾。
# ·以完成练习3-4时编写的程序为基础，在程序末尾添加一条print语句，指出哪位嘉宾无法赴约。
# ·修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。
# ·再次打印一系列消息，向名单中的每位嘉宾发出邀请。
print("\n\nI am zhu,i am sorry for that i have no time")
dinner_friend[3] = "zhang"
print("Hi,"+dinner_friend[0]+",I want to have a dinner with you")
print("Hi,"+dinner_friend[1]+",I want to have a dinner with you")
print("Hi,"+dinner_friend[2]+",I want to have a dinner with you")
print("Hi,"+dinner_friend[3]+",I want to have a dinner with you")
#完成练习3-4～练习3-7时编写的程序之一中，使用len()打印一条消息，指出你邀请了多少位嘉宾来与你共进晚餐。
print(len(dinner_friend))

# 你刚找到了一个更大的餐桌，可容纳更多的嘉宾。请想想你还想邀请哪三位嘉宾。
# ·以完成练习3-4或练习3-5时编写的程序为基础，在程序末尾添加一条print语句，指出你找到了一个更大的餐桌。
# ·使用insert()将一位新嘉宾添加到名单开头。
# ·使用insert()将另一位新嘉宾添加到名单中间。
# ·使用append()将最后一位新嘉宾添加到名单末尾。
# ·打印一系列消息，向名单中的每位嘉宾发出邀请
print("\n\nI found a bigger dinner rom")
dinner_friend.insert(0, "li")
dinner_friend.insert(3, "huang")
dinner_friend.append("huang")
print("Hi,"+dinner_friend[0]+",I want to have a dinner with you")
print("Hi,"+dinner_friend[1]+",I want to have a dinner with you")
print("Hi,"+dinner_friend[2]+",I want to have a dinner with you")
print("Hi,"+dinner_friend[3]+",I want to have a dinner with you")
print("Hi,"+dinner_friend[4]+",I want to have a dinner with you")
print("Hi,"+dinner_friend[5]+",I want to have a dinner with you")
print("Hi,"+dinner_friend[6]+",I want to have a dinner with you")

# 缩减名单：你刚得知新购买的餐桌无法及时送达，因此只能邀请两位嘉宾。
# ·以完成练习3-6时编写的程序为基础，在程序末尾添加一行代码，打印一条你只能邀请两位嘉宾共进晚餐的消息。
# ·使用pop()不断地删除名单中的嘉宾，直到只有两位嘉宾为止。每次从名单中弹出一位嘉宾时，都打印一条消息，让该嘉宾知悉你很抱歉，无法邀请他来共进晚餐。
# ·对于余下的两位嘉宾中的每一位，都打印一条消息，指出他依然在受邀人之列。
# ·使用del将最后两位嘉宾从名单中删除，让名单变成空的。打印该名单，核实程序结束时名单确实是空的。
print("I am sorry for that I have remove")
removed = dinner_friend.pop()
print(removed, ",i am so sorry")
removed = dinner_friend.pop()
print(removed, ",i am so sorry")
removed = dinner_friend.pop()
print(removed, ",i am so sorry")
removed = dinner_friend.pop()
print(removed, ",i am so sorry")
removed = dinner_friend.pop()
print(removed, ",i am so sorry")
print(dinner_friend[0])
print(dinner_friend[1])
del dinner_friend[0]
del dinner_friend[0]
print(dinner_friend)

