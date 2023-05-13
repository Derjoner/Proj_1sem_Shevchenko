class Nikola:
    
    name="Николай"
    
    let=70
    
    def __init__(self, name="Николай", let=70):
        inst = super().__init__(self, name, let)
        inst.__frozen = True
        self.name = name
        self.let = let
        
        if self.name != "Николай":
            self.name = f"Я не {self.name}, а Николай"
            print(self.__dict__)
    
    def __setattr__(self, key, value):
        if self.__frozen and not hasattr(self, key):
            raise TypeError("Нельзя!")
            super().__setattr__(key, value)
            
ni = Nikola("Максим", 12)
