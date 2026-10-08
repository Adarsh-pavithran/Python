# Encapsulation

# Encapsulation in Python is the object-oriented programming (OOP) practice of bundling data (attributes) and methods together into a single unit (a class) while restricting direct external access

# class Student:
#     def __init__(self):
#         self.name = "john"    #public
#         self._age = 20          #protected
#         self.__password = "382729"  #private

# def show_password(self):
#     print(self.__password)

# stu = Student()
# print(stu.name)
# print(stu._age)

# print(show_password)

# getter and setter

class Student:
    def __init__(self):
        self.__name = "john"    #private

        # getter method

    def get_name(Self):
        return Self.__name

        # settter method

    def set_name(self , name):
        self.__name = name

stu = Student()

# print(stu.get_name())

stu.set_name("riya")

print(stu.get_name())







        