class CurrencyConverter:
    exchange_rate = 1.0
    
    def __init__(self, amount):
        self.amount = amount
        self.exchange_rate = CurrencyConverter.exchange_rate
    
    def convert(self):
        return self.amount * self.exchange_rate
    
    @staticmethod # декоратор - вказує, що метод не використовує атрибути класу
    def set_exchange_rate(rate):
        CurrencyConverter.exchange_rate = rate


class Transport:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    
    def move(self):
        print(self.name, "рухається зі швидкістю", self.speed)
    
    @classmethod
    def create(cls, name, speed):
        print("Створено новий транспорт")
        return cls(name, speed)




if __name__ == '__main__':
    
    # converter = CurrencyConverter(100)
    # print(converter.convert())
    
    # CurrencyConverter.set_exchange_rate(28.0)
    
    # print(converter.convert())


    t = Transport.create("Car", 100)
    t2 = Transport.create("Plane", 1000)
    t3 = Transport.create("Ship", 50)
    
    t.move()
    t2.move()
    t3.move()
    t3