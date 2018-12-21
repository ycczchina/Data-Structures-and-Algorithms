# Uses python3
import sys

def get_change(m):
    #write your code here
    count = 0
    while(m >= 10):
    	m -= 10
    	count += 1
    while(m >= 5):
    	m -= 5
    	count += 1
    count += m
    return count

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
