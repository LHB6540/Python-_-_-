# 读取你刚创建的文件learning_python.txt中的每一行，将其中的Python都替换为另一门语言的名称，如C。将修改后的各行都打印到屏幕上。
file_name='learning_python.txt'
with open(file_name) as file_object:
    content=file_object.read()
    content=content.replace('Python','C')
    print(content)
with open(file_name) as file_object:
    lines=file_object
    for line in lines:
        line=line.replace('Python','C')
        print(line.rstrip())