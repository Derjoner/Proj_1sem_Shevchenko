class TriangleChecker:
    
    "Проверка отрезков для построения треугольника"
    
    storona1 = 1
    storona2 = 2
    storona3 = 3
    
    
    def is_triangle(self, storona1, storona2, storona3):
        try:
            
            self.storona1 = storona1
            self.storona2 = storona2
            self.storona3 = storona3
            
            if (self.storona1 + self.storona2 > self.storona3) and (self.storona1 + self.storona3 > self.storona2) and (self.storona2 + self.storona3 > self.storona1):
                
                print("Ура, можно построить треугольник!")
                
            elif (storona1 or storona2 or storona3) < 0:
                
                print("С отрицательными числами ничего не выйдет!")
            
            else:
                print("Жаль, но из этого треугольника не сделать.")
                
        except:
            print("Нужно вводить только числа!")
        
trey1 = TriangleChecker()
trey2 = TriangleChecker()
trey3 = TriangleChecker()
trey4 = TriangleChecker()

trey1.is_triangle(1, 2, 3)
trey2.is_triangle(2, 3, 4)
trey3.is_triangle("1", 1, 3)
trey4.is_triangle(-1, -23, 20)
