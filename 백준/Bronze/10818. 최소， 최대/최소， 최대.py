# 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.
import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
print(min(arr), max(arr))