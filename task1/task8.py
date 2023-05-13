class Prymoygolnik:
    
    dlina = 10
    shir = 10
        
    def plosh(self, dlina, shir):
        
        print(f"Площадь прямоугольника: {dlina*shir}")
    
    def perim(self, dlina, shir):
        
        print(f"Периметр прямоугольника: {dlina*2 + shir*2}")


aqwe = Prymoygolnik()

aqwe.plosh(10, 10)

aqwe.perim(10, 10)