# operator in python 

# Arithmetic operators   (+,-,*,/,%,**,//)
# Assignment operators (= , =+, )
# Comparison operators (<,> == , != , <= , >=)
# Logical operators (and, or, not)
# Identity operators (is,  not is  )
# Membership operators (in , not )
# Bitwise operators =>> skip 

# Assignment operators
x =3  # = x er vetore oi assign hoye jabe
x +=2 # x = x + 2
# print(x) 

# x = [1,3,4,8]
# print(33 in x)

# array python a oi tai list 

# array are the contained  same type or not same type multiple value in one variable 
        # 0  , 1 , 2
# a  = ['apple',34,True]

# print(a)
# add a new value after end the list
# a.append('orange')
# print(a)
# a[2] = "New Data "
# a.insert(2,"New Data") 
# print(a)

# remove item  from the list 
# a.remove('apple')  #remove is the build-in function 
# print(a)

# a.pop() #least element will deleted 
# print(a)
# ['apple', 34, 'New Data', 'New Data ', 'orange']
# find  orange position in this list 
# for data in range(len(a)):
#     if a[data] == 'orange':
#         print('The position of orange is : ',data)

# a.pop(1)
# print(a)
# a.clear()
# print(a)
# b = a.copy()

list1 = [23,22.3,5,3,45]

list2 = list1.copy()

list1.append('3435')

print(list1) # updated list ta thakbe 
print(list2) # backdated list are store in list2 