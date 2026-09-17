#  1) Without comprehention

# even_num =[]
# for i in range(1 ,11):
#     if i%2==0:
#         even_num.append(i)

# print (even_num)



# 2 )With comprehention

# even_num = [ i for i in range(1 , 11) if i%2==0 ]
# print(even_num)


#dict comprehenction

# input

# numbers =[2,3,4,5]

# output

# numbers ={
#     2:4,
#     3:6,
#     4:8,
#     5:10
# 

# square

# result ={x:x*x for x in numbers}
# print(result)



numbers=[1,2,3,4,5,6,]

result={x:x*2 for x in numbers if x%2==0}
print(result)







