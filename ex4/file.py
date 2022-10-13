# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.



from curses.ascii import isdigit



   

with open('ex4/file_encode.txt', 'r') as data:
    string = data.readline()
    print(string)
    ZipDig  = f'{string.count("w")}w{string.count("b")}b{string.count("r")}r{string.count("t")}t'
    print(ZipDig)

    
unZip = ''
zip = ''

for i in ZipDig:
    if i.isdigit():
        zip += i
    else:
        unZip += str(int(zip)* i)
        zip = ''
print(unZip)



with open('ex4/file_decode.txt', 'w') as file:
    encoded_string = ZipDig
    decoding_string = unZip
    file.write(f'{decoding_string}\n')
    file.write(encoded_string)

