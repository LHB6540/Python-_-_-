# 6-3 词汇表：Python字典可用于模拟现实生活中的字典，但为避免混淆，我们将后者称为词汇表。
# ·想出你在前面学过的5个编程词汇，将它们用作词汇表中的键，并将它们的含义作为值存储在词汇表中。
# ·以整洁的方式打印每个词汇及其含义。
# 为此，你可以先打印词汇，在它后面加上一个冒号，再打印词汇的含义；
# 也可在一行打印词汇，再使用换行符（\n）插入一个空行，然后在下一行以缩进的方式打印词汇的含义。

diction1 = {'github': 'a web for realse control', 'Google': 'a web for search'}
print('github:\n\t' +
    diction1['github'] +
    '\nGoogle:\n\t' +
    diction1['Google'])