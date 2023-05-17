# abspath - Глобальный путь к файлу


"F:\DotPack Projects\HILLEL\Courses2\PythonScriptTimEnought\lesson4\lesson4.py"

import os # os - операционная система (файловая система)
import sys # sys - системные переменные и функции


print(os.listdir()) # listdir - список файлов в текущей директории


# PATH = 'lesson4/lesson4.py'

# if os.path.exists(PATH):
#     print('Файл існує')    
# else:
#     print('Файл не існує')
#     os.mkdir(PATH) # mkdir - створити директорію
#     print('Файл створено')


# if os.path.isdir(PATH): # isdir - це директория?
#     print('це директория')
# else:
#     print('це не директория')

# os.rmdir(PATH) # rmdir - видалити директорію, якщо вона пуста
# os.remove(PATH) # remove - видалити файл


# print(sys.version) # версия Python


# my_file = open('text.txt', 'w',encoding="utf-8")    # open - відкрити файл (w - write, r - read, a - append, b - binary)
# my_file.write('Hello world\n')
# my_file.write('Hello world\n')
# my_file.write('Hello world\n')
# my_file.close() # close - закрити файл

# my_file2 = open('text.txt', 'r' )    # open - відкрити файл (w - write, r - read, a - append, b - binary)
# print(my_file2.read()) # read - прочитати файл
# my_file2.close() # close - закрити файл


# with open('text.txt', 'r' ) as my_file3: # with - контекстный менеджер, автоматически закрывает файл
#     print(my_file3.read()) # read - прочитати файл
# print('file is closed')

# # encoding - кодування файла (utf-8, cp1251, cp866, koi8-r)
# # "У" - 1043 - 0x0412 - 0b100000010010 - Кодировка UTF-8
# # "У" - 1059 - 0x0423 - 0b100000110011 - Кодировка CP1251'


# ===================== МОДУЛІ =====================

# from gtts import gTTS
  
# # This module is imported so that we can 
# # play the converted audio
# import os
  
# # The text that you want to convert to audio
# mytext = '👍🤔'
  
# # Language in which you want to convert
# language = 'uk'
  
# # Passing the text and language to the engine, 
# # here we have marked slow=False. Which tells 
# # the module that the converted audio should 
# # have a high speed
# myobj = gTTS(text=mytext, lang=language, slow=False)
  
# # Saving the converted audio in a mp3 file named
# # welcome 
# myobj.save("welcome3.mp3")



# from faker import Faker 

# fake = Faker('uk_UA') # uk_UA - українська мова

# for _ in range(10):
#   print(fake.name(), fake.address(), fake.phone_number(), fake.email(), fake.text())
#   print('=====================')


# print(fake.first_name())
# print(fake.last_name())
# print(fake.first_name_male())
# print(fake.first_name_female())
# print(fake.job())







# ===================== CLASS =====================

# class - шаблон для створення об'єктів

class Cat:
    """
    Це клас кота
    """
    # self - це об'єкт, який створюється на основі класу
    def __init__(self, name='Мурзик'):# __init__ - конструктор класу
        self.syper_var = 123
        self.name = name
        self.color = 'Невідомий'
        self._master_name = 'Вася' # _ - приватна змінна
        self.__master_last_name = 'Пупкін' # __ - приватна змінна
        
    def meow(self): # метод класу
        print(f'{self.name} говорить МЯУ МЯУ')
        
    def eat(self, food):
        print(f'{self.name} їсть {food}')
    
    def sleep(self):
        print(f'{self.name} спить')


# Наслідування класів - class Child(Parent): - клас Child наслідується від класу Parent і має всі його методи і змінні

class Tiger(Cat):
    def __init__(self, name):
        super().__init__(name) # super() - виклик батьківського класу (Cat)
        self.color = 'Золотистий'
    
    def meow(self): # перевизначення методу батьківського класу
        print(f'{self.name} говорить ГРРРР')
    
    def eat(self, food):
        print(f'{self.name} їсть {food} і п"є кров') 
        
    def run(self):
        print(f'{self.name} біжить')


tigrylya = Tiger('Тигреня')
print(tigrylya.color)
tigrylya.eat('Мясо')
tigrylya.meow()
tigrylya.sleep()
tigrylya.run()


# tom = Cat("Єжик")
# print(tom.name)
# print(tom.syper_var)
# tom.color = 'Чорного'
# print(f'Кота звати {tom.name} і він {tom.color} кольору')

# tom.meow()
# tom.eat('Молоко')
# tom.name = 'Томас'
# tom.sleep()
# tom.meow()
# tom.eat('Молоко')
# tom.lol = 'lol'
# print(tom.lol)

# print(tom._master_name)
# print(tom._Cat__master_last_name)
# print(tom.__dict__)



