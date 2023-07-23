class students:
    school = 'sarvodaya'
    batch = 2020-2023

    def __init__(self,name,age,mark):
        self.name = name
        self.age = age
        self.mark = mark

    # instance method
    def details(self):
        print(self.age,self.name,self.school,self.mark)

    # class method
    @classmethod
    def School_name(cls):
        print(cls.school)
    
    # static method
    @staticmethod
    def about_us():
        print('this is a good school')
        

s1 = students('aji',20,30)
s2 = students('abi',10,90)

students.School_name()
students.about_us()

s1.details()
s2.details()
