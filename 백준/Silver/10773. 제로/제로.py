# 재현이는 잘못된 수를 부를 때마다 0을 외쳐서, 가장 최근에 재민이가 쓴 수를 지우게 시킨다
import sys
n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    num = int(sys.stdin.readline())
    if num != 0:
        stack.append(num)
    else:
        stack.pop()

print(sum(stack))