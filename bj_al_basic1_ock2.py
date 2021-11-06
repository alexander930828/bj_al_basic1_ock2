import sys

input = sys.stdin.readline

from collections import Counter

n = int(input()) # ex) 7

aa = list(map(int, input().split())) # ex) 1 1 2 3 4 2 1

ff = Counter(aa) # ex) Counter {1: 3, 2: 2, 3: 1, 4: 1}

stack = []

ngf = [-1] * n # ex) [-1, -1, -1, -1, -1, -1, -1]


for i in range(n):
    while stack and ff[aa[stack[-1]]] < ff[aa[i]]:
        ngf[stack.pop()] = aa[i]
    stack.append(i)

print(*ngf)