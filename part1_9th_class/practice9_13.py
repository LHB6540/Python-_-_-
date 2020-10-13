# 9-13 使用OrderedDict：
# 在练习6-4中，你使用了一个标准字典来表示词汇表。
# 请使用OrderedDict类来重写这个程序，并确认输出的顺序与你在字典中添加键—值对的顺序一致
from  collections import OrderedDict
diction=OrderedDict()
diction['github']='a web for realse control'
diction['Google']='a web for search'

for key,value in diction.items():
    print(key+" :")
    print("  "+value)