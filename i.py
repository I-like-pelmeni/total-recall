import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
n = input().count(' ') + 1
print(n)