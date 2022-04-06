
#find all the numbers
#that the sum of their divisors is equal to the number itself
def find_perfect():
    number = 0
    while True:
        sum = 0
        number += 1
        for divisor in divisorGenerator(number):
            sum += divisor
            if sum == number:
                    yield number

#a generator that finds all the divisors of a number
#I got it from the web
def divisorGenerator(n):
    for i in range(1, int(n/2+1)):
        if n % i == 0:
            yield i
    yield n

#get all perfect numbers using the generator
for perfect in find_perfect():
    print(perfect)