import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
N = int(input())
a = 1
c = 1
while N[1] != N[-1] != 0:
    N[-1] = N[1]
    N = int(input())
    if N[-1] == N[1]:
        c += 1
        if c > a:
            a = c
    else:
        c = 1
print(a)