
##########################         Работа с файлами       ##################################
# 1)

f = open('directories.txt', 'r')
print(f.read())
f.close()

# 2)

log = input('Введите логин: ')
password = input('Введите пароль: ')

with open('users.txt', 'w', encoding='UTF-8') as f:
    f.write(log)
    f.write(password)


# 3)

files = open('text.txt', 'r')

if 'w' in files:
    print('да в тексте есть буква w')
else:
    print('нет, в тексте нет буквы w')


##########################    МОДУЛИ    ##################################


# 1)+

# 2)+
import random

names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
print(random.sample(names, 4))

# 3)


import os
import sys
print(os.name)
print(sys.platform)


# 4)

import sys
i = input('arguments: ')
def print_arg(a):
    print(eval(a))

print_arg(i)


# 5)

from random import randint
from os import system

for i in range(5):
    r = randint(1, 10)
    system(f'touch /Users/ajnuraomorova/Desktop/{r}.txt')


# 6)

import random


names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]

com1 = []
com2 = []
com3 = []
com4 = []
count = 1
len_com = len(names)//4

while names != []:
    name = random.choice(names)
    if count <= len_com:
        com1.append(name)
        names.remove(name)
    elif count <= len_com * 2:
        com2.append(name)
        names.remove(name)
    elif count <= len_com * 3:
        com3.append(name)
        names.remove(name)
    elif count <= len_com:
        com4.append(name)
        names.remove(name)
    count += 1

print(com1)
print(com2)
print(com3)
print(com4)

x = int(input())  # вкладываемые деньги
x1 = x
y = 10  # проценты
z = int(input())  # лет вклада

for i in range(z):
    s = x / 100 * y  # проценты на вложенную сумму
    x += s  # общая сумма

print(x)
print(int(x * 100))
print(int(x1 * pow((1 + y / 100), z) * 1000))