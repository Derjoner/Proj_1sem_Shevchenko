# 25 вариант
# Создайте класс "Машина" с атрибутами "марка", "модель" и "год выпуска". 
# Напишите метод, который выводит информацию о машине в формате "Марка: марка, Модель: модель, Год выпуска: год".

class Mashina:
    
    "Класс машин"
    
    marka = "None"
    model = "None"
    vypusk = "None"
    
    def __init__(self, marka, model, vypusk):
        
        "Инициализация машины"
        
        self.marka = marka
        self.model = model
        self.vypusk = vypusk
    
    def info(self):
        
        "Вывод информации о машине"
        
        print(f"Марка: {self.marka}, Модель: {self.model}, Год выпуска: {self.vypusk}")

pae = Mashina("Зевс", "I-23", "2004")
fakw = Mashina('Бумер', "2003153", "1989")

pae.info()
fakw.info()
