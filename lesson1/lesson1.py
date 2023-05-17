#Типи данних

# 1. int - цілі числа - 123  1  4  34  0  -1  -2  -3
# 2. float - дробові числа - 1.2  3.4  0.0  -1.2  -3.4
# 3. str - рядки - "Hello"  "World🤔"  "123"  "1.2"  "True"
# 4. bool - булеві значення - True  False
# 5. None - пусте значення - None
# 6. list - списки - [1, 2, 3, 4, [5],False,123,23.42]  ["Hello", "World", "123", "1.2", "True"]
# 7. tuple - кортежі - (1, 'lol', 3, 4, (5),False,123,23.42)  ("Hello", "World", "123", "1.2", "True")
# 8. dict - словники - {'key': {'key':[1,2,3,4]}, 'key2': 'value2'}  {"key": "value", "key2": "value2"}
# 9. set - множини - {1, 2, 3, 4, 5}  {"Hello", "World", "123", "1.2", "True"} 
# 10. frozenset - не змінні множини - frozenset({1, 2, 3, 4, 5})  frozenset({"Hello", "World", "123", "1.2", "True"})
# 11. bytes - байти - b'Hello'  b'World'  b'123'  b'1.2'  b'True' 0b10101

#Змінні - це посилання на об'єкт в пам'яті

# import sys
# print(sys.getsizeof(1))

# list_of_a = ('a','a','a','a','a','a','a','a','a','a',)
# print(sys.getsizeof(a))

# a.count('a')

# try = 123

# list_of_a
# listofa


f_sd = "Hello"
print(f_sd)

LLOL = "World"
LLOL = 'World2'

#Snake style - list_of_a
#Camel style - listOfA
#regular style - user  suma


# input("Enter your name: ")
#Задача отримати від користувача ім'я та вік, та вивести на екран привітання
# "Привіт Єгор, тобі 20 років, ти народився в 2000 році"

# a = input("Enter your name: ")



# name = input("Enter name: ")
# age = int(input("Enter age: "))
# birth_date = 2023-age

# print(f"Привіт {name}, тобі {age} років, ти народився в {birth_date} році")
# print("aboba" + str(birth_date))

# # a = 1 + '2'

# Логічні операції

# > - більше
# < - менше
# >= - більше або дорівнює
# <= - менше або дорівнює
# == - дорівнює
# != - не дорівнює

# is - перевірка на те що це один об'єкт
a = 1
b = 1
print(a is b)

# in - перевірка на наявність в списку
3 in [1,2,3,4,5]
'3' in '12345'
'34' in '012345'

# or - або
# and - і

# not - не
not '10' in '012345'
'10' not in '012345'

not True
not False

not 1==1
1!=1


#Математичні операції
# + - додавання
# - - віднімання
# * - множення
# / - ділення
# // - цілочисельне ділення
# % - остача від ділення
# ** - піднесення до степеня

#Оператори ветвлення
# if - якщо
# elif - інакше якщо
# else - інакше

if 1==1:
    print("1==1")
    
if 1==2:
    print("1==2")
else:
    print("1!=2")

if 1==2:
    print("1==2")
elif 1==1:
    print("1==1")
else:
    print("1!=2")

if 1==2:
    print("1==2")
if 1==1:
    print("1==1")
if 1!=2:
    print("1!=2")
print("Hello")

#Цикли
# while - поки
# for - для

while 1==1:
    print("1==1")

for i in range(10):
    print(i)
    
for el in 'Hello World':
    print(el)
    
import random 
    
for el in [random.randint(0,100) for i in range(10)]:
    print(el)