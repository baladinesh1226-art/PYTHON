class employee():

    def officepc(self):
        print('every employee can use office pc')

    def cab(self):
        print("can you company cab")

class manager(employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def tast(self):
        print("managint developer")

class developer(employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def tast(self):
        print("Develepling task")



manag1 = manager(name='',age=35)
emp1 = developer(name='',age=35)

manag1.cab()
emp1.cab()
manag1.tast()
emp1.tast()

