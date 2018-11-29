# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n < 1: return 0
    if n == 1: return 1

    previous = 0
    current  = 1
    sum      = [0, 1]

    for i in range(n - 1):
        previous, current = current, (previous + current) % 10
        if sum[-1] == 0 and current == 1:
            index = n % (i + 1)
            return sum[index]
        sum.append((current + sum[-1]) % 10)
    return sum[-1]

def fibonacci_partial_sum_naive(from_, to):
    sum = fibonacci_sum_naive(to) - fibonacci_sum_naive(from_ - 1)
    return sum % 10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))