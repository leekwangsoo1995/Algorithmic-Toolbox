# Uses python3
import sys

def get_optimal_value(capacity, data):
    t_cap = capacity
    t_value = 0
    for item in data:
        #print(item)
        #print(t_cap)
        #print(t_value)
        if t_cap == 0:
            return t_value
        if item[1] > t_cap:
            x = (item[1] - t_cap)
            percentage = x / item[1] 
            t_value += item[0] * (1 - percentage)
            return t_value

        else:
            t_cap -= item[1]
            t_value += item[0]

    return t_value


N, W = map(int, input().split())
#print(N)
#print(W)
#cap = N * W
xy = [map(int, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]

z = []
for i in range(N):
    z.append([x[i],y[i],x[i] / y[i]])

z = sorted(z, reverse=True, key=lambda x: x[2])
#print(x)
#print(y)
#print(z)
ret = get_optimal_value(W,z)
print(format(ret, '.4f'))
'''
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
'''