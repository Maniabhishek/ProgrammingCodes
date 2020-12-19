name="abhi"
lname='mani'
class Employee:
    name="abhi"
    lname='mani'
    def __init__(self,name,lname,pay):
        self.name = name
        self.lname = lname
        self.pay = pay
    def fullname(xx):
        return '{} {}'.format(xx.name,xx.lname)


emp1 = Employee("abhishek",'mani',5)
# print(emp1.lname)
# print(emp1.fullname())
print(Employee.fullname(emp1))