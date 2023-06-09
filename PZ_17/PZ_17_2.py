# 25 вариант
# Создайте класс "Автомобиль", который содержит информацию о марке, модели и годе выпуска. 
# Создайте класс "Грузовик", который наследуется от класса "Автомобиль" и содержит информацию о грузоподъемности. 
# Создайте класс "Легковой автомобиль", который наследуется от класса "Автомобиль" и содержит информацию о количестве пассажиров.

class Avtomobil:
    
    "Класс автомобиля"
    
    marka = "None"
    model = "None"
    vypusk = "None"
    
    def __init__(self, marka, model, vypusk):
        
        "Инициализация автомобиля"
        
        self.marka = marka
        self.model = model
        self.vypusk = vypusk
    
    def info(self):
        
        "Вывод информации о автомобиле"
        
        print(f"Марка: {self.marka}, Модель: {self.model}, Год выпуска: {self.vypusk}")
    
class Gruzovik(Avtomobil):
    
    "Класс грузовика"
    
    gruzopod = "200 кг"
    
    def get_gruzopod(self):
        
        "Вывод информации о грузоподъёмности"
        
        print(f"Грузоподъёмность: {self.gruzopod}")
    
class Ligkiy_avto(Avtomobil):
    
    "Класс лёгкого автомобиля"
    
    kol_pas = 5
    
    def get_kol_pas(self):
        
        "Вывод информации о количестве пассажиров"
        
        print(f'Количество пассажиров: {self.kol_pas}')

av1 = Avtomobil("Зверь", "П012", "1999")
av2 = Gruzovik("Грузило", "1247685", "2001")
av3 = Ligkiy_avto("Малинка", "ОР-234", "1856")

print(av1.__dict__)
print(av2.__dict__)
print(av2.get_gruzopod())
print(av3.__dict__)
print(av3.get_kol_pas())