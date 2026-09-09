# syntax

#if condition :
#   statement :

# if True:
#     print('yes')

# else :
#     print('no')

# age = int(input("Enter your age :"))

# if age > 18 :
#     print('you can vote')
# else :
#     print('you cannot vote')

# elif  used when having more than condition

# mark = int(input("Enter your mark :"))

# if mark > 85 :
#     print('A grade')
# elif mark >70 :
#     print ('B grade')
# elif mark >40 :
#     print ('C grade')
# else:
#     print("Failed")

# Nested if statement

age = 30 
is_license = True

if age > 18:
    print('you age is gratherthan 18')
    if is_license:
         print('you can drive')
    else:
        print("you cannot drive")
else:
    print("you are underage")


