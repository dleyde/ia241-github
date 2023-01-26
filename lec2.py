""" 
lec 2
IA 241, numbers, strings, variables
"""

# Wow this class is awesome

print(   type('hello')   )# comments ignored after code too
print( type (123)  )
print( type(123.123)   ) # decimal makes it a float, no decimal means integer
print(type("123."))

"""
string is a series of characters
make one with single or double quotes
strings can contain numbers letters, symbols
combo of " and ', if ' is within ", then ' is read as part of the string
if you want " to be part of the string use '
"""

print('hello')
print("hello")
print("it's 2nd python class")

"""
method is an action that can be performed on a peice of data
a dot tells python to method act on the variable. a method is followed by parenthesis to take more info
string methods:
change case: upper() and lower()
strip space on the both side of a string: strip()
split a string: split('delimiter') will return a list split based on the delimiter
addition: str + str
"""
print('Hello World'.upper())
print('Hello World'.lower())
print('    Hello World   '.strip())
print('Hello World'.split())        #default split by spaces
print('Hello World'.split('o'))     # a delimiter decides what it splits by, it has to be something already in the string
print('Hello,'+'World')

"""
integer: whole number w/o quotes
float: number with .  representing a certain level of precision
add (+) subtract (-) multiply (*) divide (/)
two multiplication symbols represent exponent
calculating integers can be different in python 2x and 3x
in 2x:
1/2 = 0
1./2 = .5
python 3 is normal
"""

print(1/2)

"""
data container
variable: store values
list: store multiple values
dictionary: store multiple values
"""

"""
variable: label refers to the python object
you can change the value of a variable in your program at any time
name of variable
    be meaningful
    cannot be python keywords
    can start with strings or underscores
    can contain numbers, strings and underscores
    use underscores to separate letters for reading purposes
"""

my_str = 'hello world'
my_int = 2
my_float = 2.0
my_num = 123

print(my_str)
print(my_int)
print(my_float)
print(my_num)

my_num = 234
print(my_num)























