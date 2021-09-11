import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
N = int(input())
if N > 0:
    if N % 2 == 0:
        print("YES", N + 2)
    else:
        print("NO", N + 1)
else: 
    print("NO", 2)