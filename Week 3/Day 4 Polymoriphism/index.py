# Method Overloading

# class MethodOverloading:
#     def method1(self):
#         print("Method1 wothout argument")
#     def method1(self,x=0):
#         print("Method with only single argument")
#     def method1(self,x=0,y=0):
#         print("Method with two argument")

# obj1=MethodOverloading()
# obj1.method1()
# obj1.method1(2)
# obj1.method1(3,4)


# Method Overriding

class University:
    def UnivName(self):
        print("Srinivas University")
    def course(self):
        print("BCA")

class Student(University):
    def course(self):
        print("MCA")

stud1=Student ()
stud1.UnivName()
stud1.course()

