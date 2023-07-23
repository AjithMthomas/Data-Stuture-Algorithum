class Vehicle:
    def __init__(self,brand,wheels):
        self.brand = brand
        self.wheels =wheels

    def start_engine(self):
        print('start engine')
    
    def open_door(self):
        print('oppenning door')


class Car(Vehicle):
# here while inheriting the parent class the child class will get all of its properties but if the child class have  init method it will give 
# priority to the child class init method so if we want  to access the parent class in init method first we want to give that parameters to the 
# init of child and call super.__init__ and pass the parameters of parent
    def __init__(self,brand,wheels,price,color):
        super().__init__(brand,wheels)
        self.price = price
        self.color = color

    def oppen_SunRoof(self):
        print('oppenning sun roof')

    def details(self):
        print(f'{self.price} {self.brand}')
        

obj = Car('bmw',4,120000,'red')
obj.open_door()
obj.details()
