import datetime
name="abhi"
lname='mani'
class Employee:
    raise_amount = 1.04
    emp_count =0

    def __init__(self,name,lname,pay):
        self.name = name
        self.lname = lname
        self.pay = pay
        Employee.emp_count +=1
    def fullname(xx):
        return '{} {}'.format(xx.name,xx.lname)

    def apply_raise(self):
        self.pay*= self.raise_amount


emp1 = Employee("abhishek",'mani',5)
emp2 = Employee("test",'user',5)
emp1.raise_amount=1.5
print(emp1.apply_raise())
print(emp1.pay)
print(emp1.raise_amount)
print(emp2.raise_amount)
# print(emp1.lname)
# print(emp1.fullname())
# print(Employee.fullname(emp1))

my_date = datetime.date(2020,12,14)
print(my_date.weekday())


