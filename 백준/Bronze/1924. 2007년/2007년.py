# 첫째 줄에 빈 칸을 사이에 두고 x(1 ≤ x ≤ 12)와 y(1 ≤ y ≤ 31)이 주어진다. 
# 참고로 2007년에는 1, 3, 5, 7, 8, 10, 12월은 31일까지, 4, 6, 9, 11월은 30일까지, 2월은 28일까지 있다.
import sys

day = 0
last_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week_list = ["SUN", "MON","TUE", "WED", "THU", "FRI", "SAT"]

m, d = map(int, sys.stdin.readline().split())

for i in range(m-1):
    day = day + last_list[i]

day += d
print(week_list[day % 7])

