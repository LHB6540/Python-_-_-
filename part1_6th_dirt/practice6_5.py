# 6-5 河流：创建一个字典，在其中存储三条大河流及其流经的国家。其中一个键—值对可能是'nile': 'egypt'。
# ·使用循环为每条河流打印一条消息，如“The Nile runs through Egypt.”。
# ·使用循环将该字典中每条河流的名字都打印出来。
# ·使用循环将该字典包含的每个国家的名字都打印出来。

river = {'nile': 'egypt', 'amazon': 'brazil', 'changjiang': 'china'}
for key, value in river.items():
    print('The ' + key + ' runs through ' + value)
    print('river:' + key)
    print('country:'+value+'\n')