import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
N = int(input())
a = [int(s) for s in input().split()]
for element in a:
    if element % 2 == 0:
        print(element, end=' ')
for element in a:
    if element % 2 != 0:
        print(element, end=' ')