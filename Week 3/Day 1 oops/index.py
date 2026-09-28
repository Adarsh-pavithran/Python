# opps concept

# 1) Class

# Class is a reusable Blueprint for creating objects.

# class
#     methods
#     attributes/variable

# Class Syntax 

    # Class Class name :
                 

# 2) object

# Objects are instence of class


# 3) oops four pillers
       
    #   Inheritance
    #   Abstraction
    #   Encapsulation
    #   Polymorphism


# class Car:
#     def drive(self ,make, model):
#         self.make = make
#         self.model = model
#         print(f"i am driving {self.make} and model is {self.model}")

# car1= Car()
# car1.drive("ford" , "mustang")
# car1.drive("BMW" , "m4")
# car1.drive("Audi" , "Q3")

# class Student():
#     school_name="ABS school"
#     def std(self , name , age):
#         self.name = name
#         self.age = age
#         print(f"My name is {self.name} and age is {self.age} and school name is {self.school_name}")

# Student1=Student()
# Student1.std("adarsh" , "22")
# Student1.std("yadhu " ,"20")



# class students():
#     school_name ="ABC school"
#     def std( self, name ,age):
#         self.name = name
#         self.age= age
#         print(f"my name is {self.name} and age is {self.age}")

# students2=students()
# students2.std("adarsh ", "22",)

# class Phones():
#     def phn( self,model ,name):
#         self.model=model
#         self.name=name
#         print(f"my model is {self.model}my name is {self.name}")

# phone1=Phones()
# phone1.phn("iphone","13",)

# for i in range(0,11):
#     print(i)

# class Base:
#     # Constructot base class

#     def __init__(self,name,roll,role):
#         self.name = name
#         self.roll = roll
#         self.role = role
#     def greet(self):
#         print('hello good morning')
    

#         # intermidiate Class : inheritage the base calss


# class Intermediate(Base):
#     def __init__ (self ,  name , role ,roll):
#         super().__init__(name , roll , role)
#         super().greet()
#         print(f"{name} {role} {role}")
       
        

# obj = Intermediate("john" , 333 , "software developer")



# Super() method

# class Emp():
#     def __init__(self , id , name , Add):
#         self.id = id
#         self.name = name
#         self.Add = Add

# class Freelance(Emp):
#     def __init__(self , id, name , Add ,Emails):
#         super().__init__(id,name,Add)
#         self.Emails = Emails
# Emp_1 = Freelance(103, "adarsh" , "kannur" , "adarshpavithran@0707@gmail.com")
# print("The Id is:" , Emp_1.id)
# print("The Name is" , Emp_1.name)
# print("The Address is" , Emp_1.Add)
# print("The Email is " , Emp_1.Emails)



