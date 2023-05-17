# Є Алфавіт, характеристики:
# 1. Мова
# 2. Список літер

# Алфавіт може:
# 1. Вивести список літер
# 2. Підрахувати кількість літер

#так само є Англійський алфавіт, характеристики:
# 1. Мова
# 2. Список літер
# 3. Кількість літер



# Для Англійського алфавіту можна:
#     1. Вивести список літер
#     2. Визначити чи являється літера англійською
#     3. Отримати приклад тексту

from faker import Faker


class Alphabet:

    def __init__(self, language: str, letters: list[str]): 
        self.language = language
        self.letters = letters
        
    def print_letters(self):
        print('Letters: ', ', '.join(self.letters))

    def len(self):  
        return len(self.letters)

    def __len__(self):  
        return len(self.letters)
    
    def __str__(self):
        return f"Alphabet {self.language} has {self.len()} letters"

class EnglishAlphabet(Alphabet):
    
    LAGUAGE = "English" 
    SHORT_NAME = "EN"
    LETTERS = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
                "j", "k", "l", "m", "n", "o", "p", "q", "r",
                "s", "t", "u", "v", "w", "x", "y", "z"]
    
    
    def __init__(self):
        super().__init__(self.LAGUAGE, self.LETTERS)
        self.number_of_letters = self.len()
        self.faker = Faker()
        
    def __str__(self):
        return 'English alphabet has {} letters'.format(self.number_of_letters)
    
    def is_letter(self, letter: str):
        return letter.lower() in self.letters

    def get_text_example(self):
        return  self.faker.text()

 

if __name__=="__main__":
    alp = Alphabet("English", ["a", "b", "c"])
    alp.print_letters()
    print(alp.len())
    print(len(alp))
    
    print(alp)
    
    a = str(alp)
    
    eng = EnglishAlphabet()
    print(eng.number_of_letters)
    print(eng.is_letter("V"))
    print(eng.is_letter("F"))
    print(eng.is_letter("Ї"))
    
    print(eng.get_text_example())
    print(eng.get_text_example())
    print(eng.get_text_example())
    
    print(eng.len())
    
    print(len(eng))

    print(eng.language)

    print(eng.letters)
    
    eng.print_letters()
    
    print(eng)