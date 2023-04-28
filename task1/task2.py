class Point:
    
    "Класс для представления координат точек на плоскости"
    
    color = 'red'
    circle = 2
    
    def set_coords(self, x=0, y=0):
        print("Вызов метода set_coords для " + str(self))
        self.x = x
        self.y = y
        
    def get_coords(self):
        print("Вызов метода get_coords для " + str(self))
        return (self.x, self.y)
    
pointOne = Point()

pointOne.set_coords(10, 20)
# print(pointOne.__dict__)

pointOne.set_coords()
# print(pointOne.__dict__)

pointTwo = Point()

pointTwo.set_coords(100, 200)
# print(pointTwo.__dict__)

# print(pointOne.get_coords())