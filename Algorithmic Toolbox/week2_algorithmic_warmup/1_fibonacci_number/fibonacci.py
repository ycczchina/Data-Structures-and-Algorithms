# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n
    else:
    	a, b = 0, 1
    	for x in range(1, n):
    		res = a + b
    		a, b = b, res
    	return res


n = int(input())
print(calc_fib(n))
