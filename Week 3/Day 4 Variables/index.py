# Instance Variable

# Static Variable / class Variable

# class Check:
#     a=100
#     def __init__(self):
#         self.b=200
# obj1=Check()
# obj2=Check()
# print("obj:1",obj1.a, obj1.b)
# print("obj 2:" , obj2.a ,obj2.b)
# Check.a=888
# obj1.b=999
# print("t1:" , obj1.a , obj1.b)
# print("t2:" , obj2.a , obj2.b)

# Static Methods

class Myclass:
    @staticmethod
    def staticmethods():  #static methods
        print("Calling of static variable")

Myclass.staticmethods()











# Instance Methods

# class MyClass:
#     def __init__(self,a1,b2,c3):  #Constructor
#         self.a1=a1
#         self.b2=b2
#         self.c3=c3
#     def avg(self):
#         return((self.a1+self.b2+self.c3))/3
# obj=MyClass(3,3,6)
# print(obj.avg())



# Class method

# class Myclass:
#     classvaraible="my class variable"
#     @classmethod
#     def classmethods(cls):  #class methods
#         return cls.classvaraible
# print(Myclass.classmethods())


    
