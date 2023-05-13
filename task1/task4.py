class Person:
    
    "Сотрудник содеражщий имя, фамилию и квалификацию"
    
    name = 'Иван'
    surname = 'Иванов'
    kvalif = 1
    
    def __init__(self, name='Иван', surname='Иванов', kvalif = 1):
        
        "Вызов метода занисение информации о сотруднике"
        
        self.name = name
        self.surname = surname
        self.kvalif = kvalif
        
    def info(self):
        
        "Вызов метода показа информации о сотруднике"
        
        print('Имя: ' + self.name + ' Фамилия: ' +  self.surname + ' Квалификация: ' + str(self.kvalif))
    
    def __del__(self):
        print("До свидания, мистер " + self.name + " " + self.surname)
    
sot1 = Person('Иван', 'Петров', 2)
sot2 = Person('Василий', 'Гуденко', 1)
sot3 = Person('Виктор', 'Фаршефохоченовский', 5)

sot1.info()
sot2.info()
sot3.info()

