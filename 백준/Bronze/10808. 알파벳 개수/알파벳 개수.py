# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각 알파벳이 단어에 몇 개가 포함되어 있는지 구하는 프로그램을 작성하시오.
import sys
S = sys.stdin.readline().strip()

arr = [0] * 26

for i in S:
    arr[ord(i) - 97] += 1
    
print(*arr)
    