"""
lab6
"""

#3.1
for i in range (0,6):
    if i != 3:
        print(i)
        
#3.2
result = 1
for i in range(1,6):
       result = result * i
print(result)

#3.3
result = 1
for i in range(1,6):
    result = result + i
print(result)

#3.4
result = 1
for i in range(3,9):
    result *= i * 8
print(result)

#3.5
numerator = 1
for i in range(8,2,-1):
        numerator *= i
print(numerator)
denominator = 1
for i in range(3,0,-1):
    denominator *= i
print(denominator)
result = numerator / denominator
print(result)

#3.6
result = 0
for word in 'this is my 6th string'.split():
    result = result +1
print(result)

#3.7
my_tweet = {
    "favorite_count": 1138,
    "lang": "en",
    "coordinates": (-75, 40),
    "entities": {"hashtags": ["Preds", "Pens", "SingIntoSpring"]}
}

num_hashtags = 0
for hashtag in my_tweet["entities"]["hashtags"]:
    num_hashtags +=1
print(num_hashtags)