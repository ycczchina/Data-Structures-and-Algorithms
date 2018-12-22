# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    left = segments[0][0]
    right = segments[0][1]
    points = [right]
    #write your code here
    for s in segments:
        if(points[-1] >= s[0] and points[-1] <= s[1]):
            left = max(left, s[0])
            right = min(right, s[1])
        elif(points[-1] > s[1]):
            right = s[1]
            points[-1] = right
        else:
            points.append(s[1])
            left = s[0]
            right = s[1]
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    segments.sort(key=lambda x: x[0])
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
