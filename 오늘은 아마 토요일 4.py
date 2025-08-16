##A = int(input("A를 입력하세요: "))
##B = int(input("B를 입력하세요: "))
##for i in range(B - 1, A - 1, -1):
##    print(i, end=' ')


##n = int(input("리스트 크기 n을 입력하세요: "))
##arr = list(map(int, input("리스트 원소를 입력하세요: ").split()))
##for i in range(1, n + 1):
##    if i % 3 == 0:

##s_list = list(input())
##idx = 1
##for i in range(len(s_list)):
##    if s_list[i] == '*':
##        s_list[i] = str(idx)
##        idx += 1
##for c in s_list:
##    print(c, end=' ')

##string = input()
##for c in string:
##    if int(c) % 2 == 1:
##        print(c, end='')

##s = input()
##check = 0
##for i in range(len(s)):
##    if s[i] == 'a' or s[i] == 'e':
##        check = 1
##if check == 0:
##    print('0')
##else:
##    print('1')

##
##N = int(input())
##arr = list(map(int, input("리스트 요소들을 입력하세요: ").split()))
##for i in range(N):
##    print(arr[i], end='')
##    if i (!= N - 1):
##        print("\\\\", end='')


##s = (input())
##n = int(input())
##print(s*n)

N = int(input("입력: "))
for i in range(N):
    b_count = i
    a_count = 2 * N - 2 * b_count
    line = 'b' * b_count + 'a' * a_count + 'b' * b_count
    print(line)








