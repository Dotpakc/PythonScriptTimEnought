# # Анатолію в останній місяць успіх посміхався дуже погано.
# # У нього три рази зламали пароль.
# # Ось він і задумався над тим, що неправильно підходить до складання паролів.
# # Щоб не напружуватися більше і знову не потрапити в халепу, він вирішив написати функцію на Python, яка перевірятиме його пароль на надійність.

# # Вимоги до пароля у Анатолія такі (він уважно вивчив рекомендації знавців):
# # 1) Довжина – від 8 до 12 символів (якщо менше – то простіше зламати, а якщо довше – то складно запам'ятати)
# # 2) У паролі повинні бути великі літери, малі символи, числа та спеціальні знаки (з переліку «*-#»; інші спецсимволи неприпустимі, оскільки Анатолій їх не може запам'ятати).


# # Напишіть програму, яка приймає пароль через input та перевіряє його на відповідність вимогам.
# # У разі правильного пароля виведеться на друк «Пароль ідеальний», а в інших випадках ви повинні вивести на друк словник (dict), де будуть перераховані всі помилки, яких Анатолій припустився.

# # Підказки:
# #  - Рядки з літерами/цифрами/символами треба перетворити на список або кортеж щоб за ними було зручно шукати
# #  - Використовуйте цикл для вибору кожного символу пароля


# def check_password(password):
#     errors = {}
      
#     if len(password)<8 or len(password)>12:
#         errors['length'] = 'Пароль повинен бути від 8 до 12 символів'
#     if not any(char.isdigit() for char in password):
#         errors['digit'] = 'Пароль повинен містити цифри'
#     if not any(char.isupper() for char in password):
#         errors['upper'] = 'Пароль повинен містити великі літери'
#     if not any(char.islower() for char in password):
#         errors['lower'] = 'Пароль повинен містити малі літери'
#     if not any(char in '*-#' for char in password):
#         errors['special'] = 'Пароль повинен містити спеціальні символи *-#'
#     return errors

# # any([True, False, False]) - ця функція перевіряє чи є хоча б один елемент в списку True
# # 3 in [1,2,4]

# # password = input('Введіть пароль: ')

# # answer_dict = check_password(password)

# # if not answer_dict:
# #     print('Пароль ідеальний')
# # else:
# #     print('Пароль не ідеальний')
# #     for key, value in check_password(password).items():
# #         print(f'{key}: {value}')
    
    


# #Цикл While
# # while - це цикл з передумовою. Цикл буде виконуватися доти, доки виконується певна умова. 
# # Як тільки умова стає невірною, цикл завершується.

# import random

# # a = 0
# # while a < 10:
# #     print(a)
# #     a += 1
    
# # for i in range(10):
# #     print(i)

# # a = 0
# # while a<10:
# #     print(a)
# #     r = random.randint(0, 2)
# #     if r == 2:
# #         a -= 1
# #     a += 1

# a= 0
# while True:
#     print(a)
#     if a >1000:
#         break
#     a += 1
# print('Цикл завершено')

# a= 0
# while True:
#     a += 1
#     print(a)
#     if a >1000:
#         break
#     if a % 2 == 0:
#         print('Парне число')
#         continue
#     print('Непарне число')
 
 
# for i in range(10):
#     if i == 5:
#         continue
#     print(i)
    
# for i in range(10):
#     for j in range(10):
#         if j == 5:
#             break
#         print(i, j)
#     if i == 5:
#         break  

# # break - завершує цикл
# # continue - переходить на наступну ітерацію циклу


# def name(a, b, c): # a, b, c - це обов'язкові аргументи
#     return a + b + c

# def name(a, b, c=10): # a, b - це обов'язкові аргументи, c - необов'язковий аргумент
#     return a + b + c

# def name(a=1, b=2, c=10): # a, b, c - необов'язкові аргументи
#     return a + b + c
   
# def name(a, b, *arg): # *arg - це необов'язкові аргументи, які будуть зберігатися у кортежі
#     return a + b + sum(arg)
# def name(a,b,**kwargs): # **kwargs - це необов'язкові аргументи, які будуть зберігатися у словнику
#     print(kwargs)
#     return a + b + sum(kwargs.values())

# name(1,2, c=10, d=20, e=30, f=40, g=50)




# # Try/Except - це конструкція, яка дозволяє перехопити помилки, які виникають у програмі.

# try:# спробуй виконати цей код
#     age = int(input('Введіть ваш вік: '))
#     print(age)
#     if age>18:
#         raise Exception('УПС!')
# except ValueError:# якщо виникла помилка ValueError, то виконай цей код
#     print('Ви ввели не число')
# except: # якщо виникла будь-яка інша помилка, то виконай цей код
#     print('Виникла помилка')
#     age=18
# else: # якщо помилки не виникло, то виконай цей код
#     print('Все пройшло добре')
# finally: # цей код буде виконуватися завжди
#     print('Програма завершена')  

# print(age)
# # print('Програма завершена')

# # raise Exception('Ви ввели не число')

# # raise - це ключове слово, яке дозволяє викинути помилку.
# # raise Exception('Ви ввели не число')
# # a = 0

# # while a<100000000:
# #     a += 1
# #     if a == 1000:
# #         raise Exception('УПС!')
# #     print(a)

# import random
# from random import randint

# from random import randint as rint
# import random as r
# from random import *
# from random import randint #, choice, shuffle

# import - це ключове слово, яке дозволяє підключити модуль у програму.
# from - це ключове слово, яке дозволяє підключити певні функції з модуля у програму.


# from math import pi

# print(pi)
# # print(randint(0, 10))
# # print(rint(0, 10))
# # print(choice([1,2,3,4,5,6,7,8,9,0]))
# # print(r.randint(0, 10))
# print(random.randint(0, 10))



# from mymod import pi, API_KEY
# import mymod
# from mymod import suma as s
# from utils import myfunc

# from mymod import aa as a, bb as b, cc as c



# print(mymod.pi)

# print(mymod.API_KEY)

# print(myfunc())


# import package.utils
# print(package.utils.myfunc())


# from package.utils import myfunc

# print(myfunc())

# from .random import randint

# from .package import utils,m2

# from package.another_package import another_mod

# from package.mod2 import another_mod
# from package.mod2 import lol

# from random import randint as rint
# from .random import randint

from package import *

# print(another_mod.price)

# print(randint)

# print(m2.lol)
# print(utils.myfunc())



if __name__ == "__main__":
    print("Я запущений як скрипт")