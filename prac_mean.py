import numpy as np

if __name__ == '__main__':
    a,b=map(int, input().split())
    print(int(np.ceil((a+b)/2)))
