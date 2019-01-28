import numpy as np

if __name__ == '__main__':
    a,b,c,x = map(int, [input() for i in range(4)])
    num = x//500
    ans = 0
    for i in range(num+1):
        ans += (x-500*i)//100 + 1
    print(ans)
