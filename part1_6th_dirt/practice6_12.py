# 6-12 扩展：
# 本章的示例足够复杂，可以以很多方式进行扩展了。
# 请对本章的一个示例进行扩展：添加键和值、调整程序要解决的问题或改进输出的格式。

#use practice6_3.py
diction = {'github': 'a web for realse control', 'Google': 'a web for search'}
print('github:\n\t' +
    diction['github'] +
    '\nGoogle:\n\t' +
    diction['Google'])

#change 
for key, value in diction.items():
    print(key+':'+value+'\n')