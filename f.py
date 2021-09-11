import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
N = int(input())
N2 = abs(N)
while N2 > 0:
    a = N2 % 10
    N2 = N2 // 10
    N3 = N2 * 10 + a
if N < 0:
    N3 * -1
print(N3)