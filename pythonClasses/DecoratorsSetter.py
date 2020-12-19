class Employee:
    
    def __init__(self,name,lname):
        self.name = name
        self.lname = lname
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.name,self.lname)
    @property
    def fullname(xx):
        return '{} {}'.format(xx.name,xx.lname)

    @fullname.setter
    def fullname(self,str):
        first ,last =str.split(' ')
        self.name = first
        self.lname = last
        return '{} {}'.format(first,last)
    @fullname.deleter
    def fullname(self):
        print('deleting')
        self.name = None
        self.lname = None
    


emp1 = Employee('test','user')
emp1.name='jim'

emp1.fullname = 'Corey schfer'

print(emp1.name)
print(emp1.email)
print(emp1.fullname)
del emp1.fullname
print(emp1.name)

print(emp1)