# 1) iterator

# An iterator is an object that gives you a value one at  a time
# it uses :
#         iter() => create an iterator
#         next() => gets the next value

# numbers = [10 , 20 , 30 ]
# my_iterator = iter(numbers)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator)) # Stop Iteration


#  2) Generator

# def numbers():
#     yield 20
#     yield 30
#     yield 40
# for num in numbers():
#     print(num)

# # decorator

# A decerator is a function that modify or adds behavior to another function without changing its orginal code 

def my_decor(function):
    def wrapper():
        print('before')
        function()
        print("after")
    return wrapper


@my_decor
def hello():
    print('hello world')
hello()

 








