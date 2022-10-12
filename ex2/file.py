# # 2. Создайте программу для игры с конфетами человек против человека.

# # Правила: На столе лежит 150 конфет.
# # Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# # За один ход можно забрать не более чем 28 конфет.
# # Все конфеты оппонента достаются сделавшему последний ход.
# # Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# # a) Добавьте игру против бота
# # b) Подумайте как наделить бота 'интеллектом'


from itertools import count
from random import randint, random


# print('Итак приветствую тебя в нашей игре! Сладкоежка')
# print()

# inter_symbol = input('Ты готов ? если да нажми "y" ')
# y = 'y'

# if inter_symbol == y:
#     print('Поехалииии!')
# elif inter_symbol != y:
#     print('Нажми на латинскую букву "y"')
#     while inter_symbol != y:
#         if inter_symbol != y:
#             inter_symbol = input('Жмиии Y ')
    

# print()

# player1  = input('Как тебя зовут игрок№1: ')
# player2  = input('Как тебя зовут игрок№2: ')

# print()



# print('Щас мы определим кто будет ходить первым')



# x = randint(1, 2)
# if x == 1:
#     lucky = player1
#     loser = player2
# else:
#     lucky = player2
#     loser = player1

# print(f'Поздравляю {lucky} ты ходишь первым !')

# print()

# print('За раз можно взять 28 конфет')
# print()

# max_take = 28

# total_candy = 150

# count = 0

# while total_candy > 0:
#     if count == 0: 
#         select1_candy = int(input(f'{lucky} cколько хапонешь конфеток ? '))
#         if select1_candy > max_take:
#             select1_candy = int(input(f'{lucky} Можно только 28'))
#         total_candy = total_candy - select1_candy
        
#     if total_candy > 0:
#             print(f'\nна кону еще {total_candy}')
#             count = 1
#     else:
#         print('Все кончились конфетки')
    
#     if count == 1: 
#         select2_candy = int(input(f'{loser} cколько хапонешь конфеток ? '))
        
#         if select2_candy > max_take:
#             select2_candy = int(input(f'{loser} Можно только 28'))
#         total_candy = total_candy - select2_candy
        
#     if total_candy > 0:
#             print(f'\nна кону еще {total_candy}')
#             count = 0
#     else:
#         print('Все кончились конфетки')



# if count == 1:
#     print(f'{loser} ПОБЕДИЛ')
# if count == 0:
#     print(f'{lucky} ПОБЕДИЛ')


# Bot vs man ------------------------------------------------------------------

print('Итак приветствую тебя в нашей игре! Сладкоежка')
print()

print()

player1  = input('Как тебя зовут игрок: ')
player2  = 'bot'

print()

print('Щас мы определим кто будет ходить первым')


x = randint(1, 2)
if x == 1:
    lucky = player1
    loser = player2
else:
    lucky = player2
    loser = player1

print(f'Поздравляю {lucky} ты ходишь первым !')

print()

print('За раз можно взять 28 конфет')
print()

max_take = 28

total_candy = 150

count = 0

while total_candy > 0:
    bot  = randint(0, 29)
    if count == 0:
        if lucky == 'bot':
            print('Ход Терминатора')
            select1_candy = bot
            print(select1_candy)
            total_candy = total_candy - select1_candy
        elif lucky == player1:
            select2_candy = int(input(f'Твой ход {lucky} '))
            total_candy = total_candy - select2_candy
            
        if total_candy > 0:
            print(f'\nна кону еще {total_candy}')
            count = 1
    else:
        print('Все кончились конфетки')
    
    if count == 1:
        if loser == 'bot':
            print('Ход Терминатора')
            select1_candy = bot
            print(select1_candy)
            total_candy = total_candy - select1_candy
        elif loser == player1:
            select2_candy = int(input(f'Твой ход {loser} '))
            total_candy = total_candy - select2_candy
            
        if total_candy > 0:
            print(f'\nна кону еще {total_candy}')
            count = 0
    else:
        print('Все кончились конфетки')

if count == 1:
    print(f'{loser} ПОБЕДИЛ')
if count == 0:
    print(f'{lucky} ПОБЕДИЛ')