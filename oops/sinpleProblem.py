# create a class for storing the details of a student
class Student:
    def __init__(self,name,age,marks:dict):
        self.name = name
        self.age = age
        self.marks = marks

    def Percentage(self):
        total=0
        count=0
        for i in self.marks.values():
            total += i
            count += 1
        percentage = (total*100)//300
        return percentage
    

s1 = Student('aji',13,{'phy':40,'che':56,'maths':99})
print(f'percentage is:{s1.Percentage()}%' )
            
