'''
#### normal for loop
def create_cubes(n):
    result=[]
    for x in range(n):
       result.append(x**3)
    return result
print(create_cubes(10))


#### generator

def cube(n):
    for x in range (n):
        yield(x**3)
print(cube(5))




##### fibonicis series imp for interviwe

def gen_fib(n):
    a=1
    b=1
    for i in range(n):
        yield a
        a,b=b,a+b
for number in gen_fib(10):
 print(number)




#### e.g

def generator():
    for x in range(3):
        yield(x)

for number in generator():
    print(number)



#### generator object
def generator():
    for x in range(3):
        yield(x)

g=generator()
print(next(g))
print(next(g))
print(next(g))


'''


#### random number between low to high

import random
def random_number(low,high,n):
    for i in range(n):
        yield random.randint(low,high)
for number in random_number(1,10,12):
    print(number)


