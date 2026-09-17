# Exeption handling

# 1) try-exept

# try :
#      a = 10
#      b = 30
#      print( a / b)
# except ZeroDivisionError :
#      print("you can't divisible by zero")
# except:
#      print("invalid result")
# else:
#      print("yes , correct")
# finally : 
#      print(" i always run")



# 2) try-exept-else

# else => runs when there is no error


# 3) try-exept-finally => it always display





# try:
#     value = int(input("Enter a number : "))
#     print (100 / value)
# except ZeroDivisionError:
#     print("you can't divisible by zero")
# except ValueError:
#     print("you can't divisible by string")
# else:
#     print("you get result")
# finally:
#     print(" i am runnig")

#  4 ) Raise

age = 100
if age < 18:
    raise ValueError("age must be greater than 18")
print("eligible")














