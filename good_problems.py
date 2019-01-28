import numpy as np

def zero_prob():
    a = int(input())
    b,c = map(int,input().split())
    # s = str(input())
    print(a+b+c,input())


def first():
    a,b=map(int,input().split())
    # num = a*b
    #1ならTrue,0ならFalseと受け取ってくれる
    if (a*b)%2:
        print('Odd')
    else:
        print('Even')

# def second():
#     s1,s2,s3 = map(int,input().split(''))
#     print(s1+s2+s3)

def second():
    print(input().count('1'))

#これムズイ
def third():
    N=int(input())
    a=list(input().split())
    for i in a:
        # binでbinaryに変換(8なら1000)した後、
        # 1が右から何番目に出現するか(4)を出し、１を引く
        # これにより、右から０が何個続くかがわかる
        ans = min(ans, bin(i).rfind('1') - 1)
    print(round(ans))

def fourth():
    # a=int(input())
    # b=int(input())
    # c=int(input())
    # x=int(input())
    a,b,c,x = map(int, [input() for i in range(4)])
    num = x//500
    ans = 0
    for i in range(num+1):
        ans += (x-500*i)//100 + 1
    print(ans)

def fifth():
    n,a,b = map(int, [input() for i in range(3)])
    ans = 0
    for i in range(n+1):
        # strをmapにして各桁を別個に保存したのち
        # listにしてsumすることで各桁の和を取っている
        if a <= sum(list(map(int, list(str(i))))) <= b:
            ans += i
    print(ans)


    
