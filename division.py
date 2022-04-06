
#find a
def find_perfect(upper_bound=10_000):
    for number in range(1, upper_bound):
        sum = 0
        for divisor in divisorGenerator(number):
            sum += divisor
            if sum == number:
                    yield number


def divisorGenerator(n):
    for i in range(1, int(n/2+1)):
        if n % i == 0:
            yield i
    yield n


for perfect in find_perfect():
    print(perfect)