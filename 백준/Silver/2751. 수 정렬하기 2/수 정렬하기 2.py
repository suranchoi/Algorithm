# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

import sys

n = int(sys.stdin.readline())
sort_list = []

for _ in range(n):
    num = int(sys.stdin.readline())
    sort_list.append(num)
    
sort_list.sort()

for i in range(len(sort_list)):
    print(sort_list[i])