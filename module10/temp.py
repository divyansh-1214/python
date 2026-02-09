print("i love you")
class student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
    def study(self):
        print("Student is studying")
        print(self.name,self.roll)

s1 = student("Divyansh", 101)
# print(s1.roll)
s1.study()
