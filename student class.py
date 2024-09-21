class Student():
    def __init__(self,name,age,schcool,uniform):
        self.name = name
        self.age = age
        self.school = schcool
        self.unfirform = uniform
        print("Hello, I am a student.")        
    def b1(self):
        print("My grades are above average in this school!")

        
student1 = Student("John",16,"Steps primary school","Black jumper with white shirts and black trousers")
student2 = Student("Mohammed",12,"Sir roberts school","blue jumpers with grey trousers and black shoes")
student1.b1()
print(student1.age)
print(student2.name)