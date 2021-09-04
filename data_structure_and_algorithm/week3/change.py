# Uses python3
import sys

def get_change(m):
    #write your code here
    cnt = 0
    if m == 0:
        return 0
    if (m / 10)  >= 1:
        cnt = int(m / 10)
        m = m % 10
    if (m / 5) >= 1:
        cnt += int(m / 5)
        m = m % 5
    cnt += m 

    return cnt


m = int(input())
print(int(get_change(m)))
