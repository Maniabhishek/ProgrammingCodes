class Employee:
    raise_amount =1.04
    def __init__(self, first , last , pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.'+last+'@company.com'
    
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def applyRaise(self):
        self.pay *= self.raise_amount

    @classmethod
    def from_string(cls , str):
        first , last , pay = str.split('-')
        return cls(first,last,pay)

class Developer(Employee):
    raise_amount = 1.10
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
    @classmethod
    def from_string(cls, str, prog_lang ):
        first , last , pay = str.split('-')
        return cls(first,last,pay ,prog_lang)
class Manager(Employee):
    def __init__(self, first, last, pay,employees=None):
        super().__init__(first, last, pay)
        if employees == None:
            self.employees == []
        else :
            self.employees = employees
    def add_emp(self,emp):
        self.employees.append(emp)
    def remove_emp(self,emp):
        self.employees.remove(emp)

    def empName(self):
        for emp in self.employees:
            print(emp.fullname())




dev1 = Developer.from_string("john-doe-20",'javascript')
print(dev1.email)

dev2  = Developer('test', 'user', 40,'python')
print(dev2.email)

mg1 = Manager('test2','user',10,[dev1,dev2])
print(mg1.email)

mg1.empName()

mg1.add_emp(dev1)
# print(mg1.empName())