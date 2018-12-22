# Uses python3
import sys
import math

def optimal_summands(n):
    #write your code here
    x = int((-1 + math.sqrt(1 + 8 * n)) / 2)
    summands = [i for i in range(1, x)]
    summands.append(int(n - (x + 1) * x / 2 + x))
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
