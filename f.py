import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
N = int(input())
N = abs(N)
while abs(N) > 0:
    a = abs(N) % 10
    b = abs(N) - a
    M = b * 10 + a
if N < 0:
    M * -1
print(M)