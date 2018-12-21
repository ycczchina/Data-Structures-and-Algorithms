# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    data=[(w, v) for w, v in zip(weights,values)] 
    data.sort(key=lambda x: (-x[1] / x[0]))
    i = 0
    while(capacity > 0 and i < len(data)):
    	a = min(data[i][0], capacity)
    	value += a * data[i][1] /data[i][0]
    	capacity -= a
    	i += 1
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
