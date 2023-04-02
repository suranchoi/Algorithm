'''
첫째 줄에 피연산자의 개수(1 ≤ N ≤ 26) 가 주어진다. 그리고 둘째 줄에는 후위 표기식이 주어진다. 
(여기서 피연산자는 A~Z의 영대문자이며, A부터 순서대로 N개의 영대문자만이 사용되며, 길이는 100을 넘지 않는다) 
그리고 셋째 줄부터 N+2번째 줄까지는 각 피연산자에 대응하는 값이 주어진다. 3번째 줄에는 A에 해당하는 값, 4번째 줄에는 B에 해당하는값 , 5번째 줄에는 C ...이 주어진다, 그리고 피연산자에 대응 하는 값은 100보다 작거나 같은 자연수이다.
'''
import sys

N = int(sys.stdin.readline())
expression = list(sys.stdin.readline().strip())
num = [int(sys.stdin.readline()) for i in range(N)]
stk = []

for i in expression:
    if i.isalpha():
        stk.append(num[ord(i) - 65])
    else:
        a = stk.pop()
        result = stk.pop()
        if i == "+":
            result+=a
        elif i == "-":
            result-=a
        elif i == "*":
            result*=a
        elif i == "/":
            result/=a
        stk.append(result)

print('%.2f' %stk[0])