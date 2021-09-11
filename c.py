import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
for i in range(5):
    (a, b, c) = [int(s) for s in input().split()]
    if a >= 0 and a <= 23 and b <= 59 and b >= 0 and c <= 59:
        print("YES")
    else:
        print("NO")