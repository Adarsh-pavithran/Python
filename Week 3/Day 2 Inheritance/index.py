# Inheritance

# class Parents:
#     name ="adarsh"
#     def eat(self):
#         print("parent can eat")

# class Child(Parents):
#     def sleep(self):
#         print("child can sleep")
    
     

# c1 = Child()
# c1.eat()
# c1.sleep()
# print(c1.name)


# class Animal:
#     def eat(self):
#         print("Animal can eat")

# class Dog(Animal):
#     def bark(self):
#         print("Dog can bark")

# c1 = Dog()
# c1.eat()
# c1.bark()


# 1) Single level inheritance

# parent class = Base class

# Child class = Derived class


# Multi level Inheritance

# class Grandparent:
#     def walk(self):
#         print("i can walk, i am grand parent")

# class Parent(Grandparent):
#     def eat(Self):
#         print("parent can eat")

# class Child(Parent):
#     def sleep(self):
#         print("child can sleep")

# c1 =Child()
# c1.eat()
# c1.sleep()
# c1.walk()

# Multiple inheritance


# class Grandparent:
#     def walk(self):
#         print("i can walk, i am grand parent")

# class Parent:
#     def eat(Self):
#         print("parent can eat")

# class Child( Grandparent , Parent ):
#     def sleep(self):
#         print("child can sleep")

# c1 =Child()
# c1.eat()
# c1.sleep()
# c1.walk()


# Hiearchial Inheritance

# class Parent():
#     def eat(Self):
#         print("parent can eat")

# class Child1(Parent):
#     pass

# class Child2(Parent):
#     pass

# class Child3(Parent):
#     pass

# c1 = Child1()
# c1.eat

# c2 = Child2()
# c1.eat



# class Parent():
#     def eat(Self):
#         print("parent can eat")


# class Child1(  Parent ):
#     def sleep(self):
#         print("child can sleep")

# class Child2(   Parent ):
#     def eat(self):
#         print("child can eat")

# class Child3(  Parent ):
#     def walk(self):
#         print("child can walk")

# c1 = Child1()

# c1.sleep()
# c1.eat()

# c1 = Child2()

# c1.eat()

# c1 = Child3()
# c1.walk()

# c1.eat()


# Hybried Inheritance


# class Animal:
#     def speak(self):
#         print("Animal speaks")

# class Mammel(Animal):
#     def give_birth(Self):
#         print("Mamal givrs birth")

# class Bird(Animal):
#     def lay_eggs(Self):
#         print("Bird lays eggs")

# class platypus(Mamal , Bird):
#     pass


# platypus = platypus()
# platypus.speak()
# platypus.give_birth()
# platypus.lay_eggs()


# magic method


# class Car:
#     def __init__(self,make,model):
#         self.make = make
#         self.model = model
#         # print(f"car model is{self.model}")
#         # print(f"car name is {self.make}")

#     def drive(self):
#         print(f"iam driving {self.make} and the car model is {self.model}")

# c1 = Car("ford" , "mustang")
# c1.drive()



# class Students:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print(f"my name is {self.name} and my age is {self.age}")

# c1 = Students('adarsh',"22")
# c1.greet()


class Base:
    # Constructot base class

    def __init__(self,name,roll,role):
        self.name = name
        self.roll = roll
        self.role = role
    def greet(self):
        print('hello good morning')
    

        # intermidiate Class : inheritage the base calss


class Intermediate(Base):
    def __init__ (self ,  name , role ,roll):
        super().__init__(name , roll , role)
        super().greet()
        print(f"{name} {role} {role}")
       
        

obj = Intermediate("john" , 333 , "software developer")









 



