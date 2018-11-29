# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    arr = [0, 1]
    previous = 0
    current  = 1

    for i in range(n - 1):
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            index = n % (i + 1)
            return arr[index]
        arr.append(current)

    return current

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
