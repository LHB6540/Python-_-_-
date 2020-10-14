# 10-10 常见单词：
# 访问项目Gutenberg（http://gutenberg.org/），并找一些你想分析的图书。下载这些作品的文本文件或将浏览器中的原始文本复制到文本文件中,
# 你可以使用方法count()来确定特定的单词或短语在字符串中出现了多少次。
# 编写一个程序，它读取你在项目Gutenberg中获取的文件，并计算单词'the'在每个文件中分别出现了多少次。

book_name='The Story of the Bank of England.txt'
def get_number_of_word(book_name,word='the'):
    with open(book_name,encoding='UTF-8') as file_object:
        content=file_object.read()
    return content.lower().count(word)

print(get_number_of_word(book_name))