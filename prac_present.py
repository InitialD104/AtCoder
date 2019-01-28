import numpy as np

if __name__ == '__main__':
    n = int(input())
    ans = 1
    for i in range(3):
        su=sum(list(map(int, input().split())))
        # print('sum',su)
        ans = ans * su
    print(ans)
