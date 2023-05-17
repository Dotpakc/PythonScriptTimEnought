
class Entity:
    def __init__(self, name, level, health):
        self.name = name
        self.level = level
        self.health = health

    def attack(self, target):
        print(self.name, "атакує", target.name)
        target.take_damage(self.level*2)

    def take_damage(self, damage):
        self.health -= damage
        print(self.name, "зазнав", damage, "пошкоджень здоров'я")


class Monster(Entity):
    def __init__(self, name, level, health):
        super().__init__(name, level, health)
        self.team = "Monster"
    
    @staticmethod  # декоратор - вказує, що метод не використовує атрибути класу
    def roar():
        print("PPPppppppp")


class Player(Entity):
    
    player_count = 0
    
    def __init__(self, name, level, health):
        super().__init__(name, level, health)
        self.team = "Player"
        self.experience = 0
        self.gold = 0
        Player.player_count += 1
        
    
    
    def level_up(self):
        self.level += 1
        print(self.name, "піднявся на рівень")
    
    def gain_experience(self, experience):
        self.experience += experience
        if self.experience >= self.level*100:
            self.level_up()
            self.experience = 0
        print(self.name, "отримав", experience, "досвіду")
    
    def acquire_gold(self, gold):
        self.gold += gold
        print(self.name, "отримав", gold, "золота")
        
    @classmethod 
    def get_player_count(cls): # cls - клас, який викликав метод
        return cls.player_count
        
    

class Game:
    def __init__(self):
        self.monsters = []
        self.players = []
        
    def add_monster(self, monster):
        self.monsters.append(monster)
        print("До гри додано монстра", monster.name)
    
    def add_player(self, player):
        self.players.append(player)
        print("До гри додано гравця", player.name)
    
    def start():
        print("Гра почалася")
        
    def end():
        print("Гра закінчилася")
        
        
if __name__=="__main__":
    print(Player.get_player_count()) # 0

    player1 = Player("Alice", 1, 100)
    print(player1.get_player_count()) # 1

    player2 = Player("Bob", 1, 100)
    print(player2.get_player_count()) # 2
