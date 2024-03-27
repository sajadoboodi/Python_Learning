class person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    '''def get_name(self):
        print('My name is %s'% self.name)

    def get_age(self):
        print('Im %s years old'% self.age)'''

    def get_info(self):
        print('Hi :|) My name is %s and Im %s years old'% (self.name,self.age))
    
myperson = person('Sajad',20)
print(myperson.name)
print(myperson.age)
'''myperson.get_name()
myperson.get_age()'''
myperson.get_info()
myperson.age += 1
myperson.get_info()
jamshid = person('Jamshid',45)
jamshid.get_info()
print(jamshid.age)
print(myperson.age)