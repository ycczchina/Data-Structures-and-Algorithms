# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = [0, 1]

    for i in range(n - 1):
        previous, current = current, (previous + current) % 10
        if sum[-1] == 0 and (current * current) % 10 == 1:
            index = n % (i + 1)
            return sum[index]
        sum.append(((current * current) % 10 + sum[-1]) % 10)
    return sum[-1]

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_naive(n))
