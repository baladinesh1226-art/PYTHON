class teacher():

    def board (self):
        print("can use black board")


class student(teacher):
    def __init__(self , name , age ):
        self.name = name
        self.age = age


    def display(self):
        print(f"student {self.name} is {self.age} years old")


s1 = student(name = "Dinesh", age =29)
s1.display()
s1.board()