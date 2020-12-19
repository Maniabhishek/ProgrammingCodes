class Employee:
    
    def __init__(self,name,lname,pay):
        self.name = name
        self.lname = lname
        self.pay = pay
    def fullname(xx):
        return '{} {}'.format(xx.name,xx.lname)

    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.name,self.lname,self.pay)

    def __add__(self,other):
        return self.pay+other.pay
    def __len__(self):
        return len(self.fullname())



emp1 = Employee("abhishek",'mani',5)
emp2 = Employee("test",'user',6)

print(emp1)

print(emp1.__repr__())

print(emp1+emp2)
print(len(emp2))
print('-->')
print(emp2.__len__())

print(emp1.__add__(emp2))