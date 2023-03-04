"""
lab 7
while loops
"""

#3.1
num = 0
while num <=5:
    if num != 3:
        print(num)
    num+=1
    
#3.2
i=1
result=1
while i<=5:
    result = result*i
    i=i+1
print(result)

#3.3
i=1
result=0
while i <=5:
    result +=i
    i += 1
print(result)

#3.4
i=3
result=1
while i <=8:
    result *= i
    i += 1
print(result)

#3.5
num = 8
den = 3
result = 1
while num >= den:
    result *= num
    num -= 1
while den >= 1:
    result /= den
    den -= 1
print(result)
#3.6
num_list = [12, 32, 43, 35]
while num_list:
    del num_list[-1]
    print(num_list)