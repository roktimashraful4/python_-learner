# a = (1,3,4,2)

# print(a)
# print(type(a))
# print(a[0])

# we can't assign data in tuple 
# a[0] = 'data' # we got an error 

# what can i do for assign or update a value in tuple 
'''
first we convert tuple to list then update or assign a value and then agin we convert this to tuple 
'''

# a = (1,2,3,4)
# print(a) #  (1,2,3,4)
# print(type(a)) # tuple
# a = list(a)
# print(a)  #[1,2,3,4]
# print(type(a)) # list 
# a.append('new data')
# print(a)  #[1,2,3,4,'new data']
# a = tuple(a) 
# print(a)  # (1,2,3,4,'new data')
# print(type(a)) # tuple

colors = ('red','green','blue') #value tuple 

( color1, color2, color3 ) = colors # variable tuple

print(color1)