# thik that we have a company and its employees so we need company details in every employee details

class Company:
    def __init__(self,c_name,location) :
        self.c_name = c_name
        self.location = location

class Emp:
    def __init__(self,name,age,salary,comp:Company) :
        self.name = name
        self.age = age
        self.salary = salary
        self.comp = comp

    def details(self):
        print(f' name :{self.name}\n age:{self.age}\n company name:{self.comp.c_name}')


comp = Company('broto','calicut')
ss= Emp('aji',12,4000,comp)
ss.details()
