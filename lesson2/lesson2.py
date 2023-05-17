# String - строка, послідовність символів, контеєнер, колекція ітерабельний об'єкт
# Індексація - доступ до окремих елементів колекції
# Це тип даних str (string) який не змінюється, тобто якщо ми змінюємо строку, то ми створюємо нову строку

# a = 'hello world'
# print(id(a)) # id - ідентифікатор об'єкта
# a = a.capitalize()
# print(id(a)) # id - ідентифікатор об'єкта
# print(a)

# a = [1,2,3,4,5]
# print(id(a)) # id - ідентифікатор об'єкта
# a.append(6)
# print(id(a)) # id - ідентифікатор об'єкта

# a[0:3] # [1,2,3] - зріз , slice
# a[-1] # 5 - індексація з кінця
# a[0] # 1 - індексація з початку
# print(a)
# a[1:3] = [10,20]
# print(a)

# a[333333333]


# Mutable - це змінювані типи даних
# 1. list
# 2. dict
# 3. set
# 4. bytearray
# 5. user defined classes

# Immutable - це незмінювані типи даних
# 1. int
# 2. float
# 3. complex
# 4. bool
# 5. str
# 6. tuple
# 7. frozenset
# 8. bytes
# 9. user defined classes





# for i in 'hello world':
#     print(i, end=' ')
    
# print('hi', 'world','world','world','world','world', sep='|', end='!\n')

# a = str([1,2,3,4])
# print(a)
# a = ['Hello world']
# print(a)
# a = list(['Hello world'])
# print(a)
# class A:
#     pass
#     def __str__(self):
#         return 'hello world'

# a = A()

# b = str(a)
# print(b)

# def f():
#     return 'hello world'
# a = f()
# f = lambda : 'hello world'
# a = f()
# print(a)

# list methods
# .append(123) - додає елемент в кінець списку
# .extend([1,24,5]) - з'єднує два списки
# .insert(0,'HELLo') - вставляє елемент в список
# .remove(123) - видаляє елемент зі списку
# .pop(0) - видаляє останній елемент зі списку
# .clear() - очищує список
# .index(123) - повертає індекс елемента
# .count(123) - повертає кількість елементів
# .sort() - сортує список
# .reverse() - реверсує список
# .copy() - копіює список

# a= [1,2,3,4,5,6,7,8,9,10]
# a.sort(key= lambda x: x%2)
# print(a)
a = [1,2,3,4,5,6,7,8,9,10]
a[3] = 123


#tuple - кортеж, не змінюваний тип даних
# Різниця між кортежем і списком в тому, що кортеж не змінюється, а список змінюється
a = (1,2,3,4,5,6,7,8,9,10)
a = 1,2,

text, date = ('hello world', '2020-01-01')

a,b,c = 1,[1,3,4,5,67],3

a,b = b,a

print(a,c,b)

a= tuple([1,2,3,4,5,6,7,8,9,10])
print(a)
b = list(a)
b.append(11)
print(b)
a = tuple(b)
print(a)
# .count()
# .index()
len(a)


# def f():
#     name = 'hello world'
#     date = '2020-01-01'
#     return name, date

# a = f()
# print(a)

def f(count=1):
    l = []
    name = 'hello world'
    date = '2020-01-01'
    for i in range(count):
        l.append((name, date))
    return l

a = f()
print(a)
# for text,date in a:
#     print(text*2, date)
    
# for i,el  in enumerate(a):
#     print(i)
#     print(el)

# print(list(enumerate(a, start=3)))


# dict - словник, мапа, хеш таблиця, асоціативний масив, ключ:значення , JSON

# ключ:значення
a = {1,4,5,6,7,8,9,10} # set
a = {'name':'hello world', 'date':'2020-01-01'} # dict
a['name'] # 'hello world'
a['date'] # '2020-01-01'

# key - це не змінюваний тип даних
# value - це будь-який тип даних

# int 
#  {1:1, 2:2, 3:3, 4:4, 5:5}
#  a[1]
# str 
#  {'name':'hello world', 'date':'2020-01-01'}

# tuple
#  {(1,2,3):'hello world', (4,5,6):'2020-01-01'}
#  a[(1,2,3)]
# # bool
#  {True:'hello world', False:'2020-01-01'} 
    # a[True]
# float
#  a= {1.1:'hello world', 2.2:'2020-01-01'}
    # a[1.1]

a = {'name':'hello world', 'date':'2020-01-01'} # dict

# .get('name') - повертає значення по ключу
# b = a['name1'] # 'hello world'
b = a.get('name', 'asdas') # 'hello world'
print(b)

# .keys() - повертає всі ключі, які є в словнику, в форматі dict_keys
# print(a.keys())
# for key in a.keys():
#     print(key)
# print(list(a.keys())[-1])

# .values() - повертає всі значення, які є в словнику, в форматі dict_values
# print(list(a.values()))

# .items() - повертає всі пари ключ:значення, які є в словнику, в форматі dict_items
# print(list(a.items()))
# for key,value in a.items():
#     print(key, value)

a = {'name':'hello world', 'date':'2020-01-01'} # dict
# b = a.pop('name') # видаляє пару ключ:значення
# print(a)
# print(b)

# .popitem() # видаляє останню пару ключ:значення
print(a.popitem())
print(a)

user = {
    'name':'hello world',
    'age': 20,
    'hobbies': ['football', 'basketball', 'tennis'],
    'address': {
        'city': 'Lviv',
        'street': 'Shevchenka',
        'building': 1
    },
    'friends': [
        {
            'name': 'LOL', 
            'age': 20,
            'hobbies': ['football', 'basketball', 'tennis'],
            'address': {
                'city': 'Lviv',
                'street': 'Shevchenka',
                'building': 1
            }
        },
        {
            'name': 'Ivan',
            'age': 20,
            'hobbies': ['football', 'basketball', 'tennis'],
            'address': {
                'city': 'Lviv',
                'street': 'Shevchenka',
                'building': 1
            }
        }
    ]
}


# print(f'Перший друг - {user[]}')

for i,friend in enumerate(user['friends']):
    print(i,friend['name'], friend['age'])


names = ['Jone', 'Ivan', 'Oleg']
for i, name in enumerate(names,1): # (0, 'Jone')  (1, 'Ivan') (2, 'Oleg')
    print(i ,name)
    
i = 0
for name in names:
    print(i ,name)
    i += 1




#Function - функція
# def - ключове слово для створення функції
# f - назва функції 
# () - параметри функції
# : - двокрапка
# return - ключове слово для повернення значення з функції
# a,b,c - параметри функції
# a+b+c - тіло функції
# f(1,2,3) - виклик функції
# 6 - результат виклику функції

def f(a,b,c):
    return a+b+c

print(f(1,2,3))

def a():
    pass # пуста функція

def b():
    ... # пуста функція

print(a()) # None
print(b()) # None


# def win():
#     print('You win')
#     print('You win')
    
# def lose():
#     print('You lose')
    
# def draw():
#     print('Draw')
    
# win()
# lose()
# draw()
# win()
# win()
# win()



def greeting(name2):
    print(f'Hello {name2}')
    
greeting('Ivan')
greeting('Oleg')
greeting('Jone')
# greeting()

def greeting(name2='world'):
    print(f'Hello {name2}')
    
greeting('Ivan')
greeting('Oleg')
greeting('Jone')
greeting()

def greeting(name2='world', age=20):
    print(f'Hello {name2} {age}')
    
greeting('Ivan', 30)
greeting('Oleg' )
greeting('Jone', 50)

a = ("Ivan", 999)

greeting(*a) # args

def greeting(*args, name2='world', age=20):
    print(f'Hello {name2} {age}')
    print(args)

greeting(1,3,4,5, name = 'Ivan', age = 30)

print(12,312,3,124,124,124,142,124,1254,125,125,12,5,)
# print(end='\n' ,sep=' ', 12,312,3,124,124,124,142,124,1254,125,125,12,5)

def greeting():
    if True:
        return 1
    return False


# {"Error":['error1', 'error2', 'error3']}


