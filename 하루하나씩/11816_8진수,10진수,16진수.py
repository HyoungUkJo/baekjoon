""" 
정수 X가 주어진다. 정수 X는 항상 8진수, 10진수, 16진수 중에 하나이다.

8진수인 경우에는 수의 앞에 0이 주어지고, 16진수인 경우에는 0x가 주어진다.

X를 10진수로 바꿔서 출력하는 프로그램을 작성하시오.
"""

N = input()
if N.startswith('0x'):
    print(int(N,16))
elif N.startswith('0'):
    print(int(N,8))
else:
    print(N)
