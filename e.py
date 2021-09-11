import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
N = int(input())
M = int(input())
a = 1
c = 1
while N != 0 and M != 0:
    M = N
    N = int(input())
    if M == N:
        c + 1
        if c > a:
            a = c
    else:
        c = 1
print(a)