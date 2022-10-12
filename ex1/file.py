# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв""

pathRead = 'ex1/text.txt'
pathWrite = 'ex1/text2.txt'

try:
    with open(pathRead) as data:
        file = data.read().split(' ')
except:
    print('Файл ненайден')

print(file)


def del_some_words(text_file):
    text_file = list(filter(lambda x: 'абв' not in x, text_file))
    return " ".join(text_file)

result = del_some_words(file)
print(result)


try:
    with open(pathWrite, 'w') as data:
        file = data.write(result)
except:
    print('Файл ненайден')