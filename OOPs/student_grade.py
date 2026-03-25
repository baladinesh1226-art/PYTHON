class student():
    def __init__(self, name):
        self.name = name

    def grade(self, marks):
        print("the student ef")
        if marks >= 90:
            print('Grade A')
        elif marks >= 80 and marks < 90:
            print('Grade B')
        elif marks >=70 and marks < 80:
            print('Grade C')
        elif marks >=35 and marks < 70:
            print('Grade D')
        else:
            print('Grade fail')



s1 =student('James')
s1.grade(20)