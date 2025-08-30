##a,b = map(int,input(" ").split())
##
##if a<b:
##    print(a+b)
##elif a>b:
##    print(a-b)
##    
##else:
##    print(a=b)

##hap = 0
##i = 1
##n = int(input(""))
##
##while i <= n:
##    if i % 3 == 0:
##        hap += i
##    i += 1
##
##print(hap)


n = int(input(""))
arr = []
arr = input().split()
for i in range(n):
    arr[i] = int(arr[i])
for i in range(0, n, 2):
    print(arr[i])
print()
for i in range(1, n, 2):    
    print(arr[i])   

##n = int(input())
##
##arr = []
##arr = input().split()
##
##for i in range(n):
##    arr[i] = int(arr[i])
##
##print(max(arr) - min(arr))



##n = input()
##if n.islower():
##    print(n.upper())
##else:
##    print(n.lower())

##print("\"Python:\\test\"")


##n, m = map(int, input().split())
##for i in range(n):
##    print('*' * m)












