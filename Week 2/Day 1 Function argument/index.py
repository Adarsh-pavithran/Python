#Function arguments

# ----------------------------

# 1) Required aragument / Positional argument

# def add(a , b):
#     print(a+b)

# add(10 , 20)


# 2 ) Default argumnet / assign  value to parameter

# def add(a , b=40):
#     print(a+b)

# add(10 , )


#3)  Keyword arguments

# def students(name ,age):
#     print(name,age)
# students(name='adarsh' , age="22")


# 4) Arbitary argument /Return Tuple ()

# def add(a, *args):
#     print(a ,args)
# add(1,2,3,4,5,6)

# def add(*args):
#     #print(sum(args)) / Using default sum method
#     total = 0
#     for i in args:
#         total += i
#     return total
# print(add(1,2,3,4,5))


# 5) Arbitary  Keyword argument  / return dictionary {}

# def student(**kwargs):
#     print(kwargs)
#     print(kwargs['age'])
# student(name='adarsh' , age="22" , city="kannur")

# --------------------------------------------------------------------------------------------------------------------




# Normal fuction

# def square(x):
#     return x* x
# print(square(5))


#  Lambda function

# square = lambda x: x * x
# print(square(5))


# add = lambda a , b : a+b
# print(add(20 , 30))

# map() , filter(), reduce()

# numbers = [2,3,4,5]
# result = list(map(lambda x:x*2 ,numbers))
# print(result)


# square

# numbers = [2,3,4,5]
# spuare = list(map(lambda x:x* x,numbers))
# print(spuare)


# numbers =[2,3,4,5,6,7,8,9]
# result = list(filter(lambda x:x > 5 , numbers))
# print(result)

# even numbers

# numbers =[2,3,4,5,6,7,8,9]
# result = list(filter(lambda x: x%2==0,numbers))
# print(result)


# odd numbers

# numbers =[2,3,4,5,6,7,8,9]
# result = list(filter(lambda x: x%2==1,numbers))
# print(result)


# reduce

# from functools import reduce

# sum

numbers = [1,2,3,4,5]
result = reduce(lambda x , y : x + y ,numbers)
print(result)

# factorial

numbers = [1,2,3,4,5]
result = reduce(lambda x , y : x * y ,numbers)
print(result)























    









