import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
N = int(input())
a = [int(s) for s in input().split()]
a.sort()
print(a, end=' ')