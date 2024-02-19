
data  = {
    'name': 'John',
    'age': 34,
    'city': 'New York'
}


# print(data) 

# users = [ # list [1,3,4,"there"]
#     {
#         'name': 'John',
#         'age': 34,
#         'city': 'New York'
#     },
#     {
#         'name': 'Jane',
#         'age': 24,
#         'city': 'New York'
#     }
# ]


# print(users[0]['city'])


users = [ # list [1,3,4,"there"]
    {
        'name': {
            'first': 'John',
            'last': 'Doe'
        },
        'age': 34,
        'city': 'New York',
        'hobbes': ['reding', 'writing','shopping']
    },
    {
        'name': 'Jane',
        'age': 24,
        'city': 'New York'
    }
]

# users.append({
#     "name":'roktim',
#     'age': 23,
#     'city': "new York"
# })
# print(users)

user = {
    "name":'roktim',
    'age': 23,
    'city': "new York"
}

# print(user)

user['age'] = 43

# print(user)

user['name'] = 'Roktim Ashraful'

print(user)

# user.pop('age') # Remove 

print(user)

# del user['name'] # Remove 

print(user)


print(user.keys())

for i in user.keys(): # show all key name in key()
    print(i)