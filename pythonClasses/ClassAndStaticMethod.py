
@classmethod
def from_string(cls, date_as_string):
    day, month, year = map(int, date_as_string.split('-'))
    date1 = cls(day, month, year)
    return date1

# date2=Date.from_string('02-01-1997')
# print(date2)

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


new_emp1 = Employee.from_string('john-doe-20')
print(new_emp1.fullname())


