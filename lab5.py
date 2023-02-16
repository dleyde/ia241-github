"""
lab 5
gamer lab
"""

#3.1
alien_color = 'green'
if alien_color == 'green':
    print('you got 5 points!')
#3.2
alien_color = 'red'
if alien_color == 'green':
    print('you got 5 points')
else:
    print('wowza, you got 10 points!')
#3.3
favorite_fruits = ['strawberry', 'pear', 'grape']
if 'grape' in favorite_fruits:
    print("Nobody likes grapes, you're a liar")
if 'strawberry' in favorite_fruits:
    print('Strawberries are cool I guess...')
if 'pear' in favorite_fruits:
    print('Get away from me you monster')
    
#3.4
age = 99
if age<10:
    print('This person is a child')
elif 10<age<20:
    print('This person is a teenageer')
elif 20<age<65:
    print('This person is an adult')
elif 65<age:
    print('This person is an elder')