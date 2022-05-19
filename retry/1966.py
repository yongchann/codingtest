from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, target = map(int, input().split())
    prior = 