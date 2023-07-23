# by default python dont have methothd overloading ,but we can impliment it using default arguments or arbitory arguments

class Math:
    def find_sum(self,a,b,*c):
        sum = 0
        for i in c:
            sum+=i
        sum = a+b+sum
        return sum
    
obj = Math()
obj.find_sum(1,2,3,4,5)
print(obj.find_sum(1,2,3,4,5))