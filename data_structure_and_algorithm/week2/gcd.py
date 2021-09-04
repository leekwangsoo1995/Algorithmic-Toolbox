# Uses python3
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd_fast(a,b):
    ans = None
    while True:
        if b < 0 or b == 0 or a < 0 or a == 0:
            return 1
        calc = a % b 
        if calc == 0:
            return b
        a = b
        b = calc

    return prev

n = str(input())
a, b = map(int, n.split())
#print(gcd_naive(a, b))
#print("fast")
print(gcd_fast(a, b))
