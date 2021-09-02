# Uses python3
#pythonで書き直し。
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def fast_fib(n):
    ar = []
    ar.append(0)
    ar.append(1)
    if n < 2:
        return ar[n]
    
    for i in range(2,n+1):
#        print(i ,'番目')
 #       print(ar[i - 1])
  #      print(ar[i - 2])
        x = ar[i - 1] + ar[i - 2]
  #      print('x',x)
        ar.append(x)

    return ar[-1] 


n = int(input())
print(fast_fib(n))
#print('calc',calc_fib(n))
