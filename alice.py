##f = open("alice.txt", "r", encoding = "UTF8")
##book = f.read()
##n = book.count('앨리스')
##print(n)
##
##f.close()



##List = [1,3,5,7,[9,10]]
##for i in List:
##    print(i)
    

##import random
##
##List = []
##
##for _ in range(10) :
##    List.append(random.randint(1, 10))
##
##print(List)
##print(List.count(7))
##List.sort()
##print(List)
##List.reverse( )
##print(List)


f = open("Alice.txt", "r", encoding = "UTF8")
book  = f.read()
words  = input("검색하려고 하는 단어를 5개 입력해 주세요.: ")
words = words.split()
cnt = []
for word in words :
    n = book.count(word)
    print("%s : %d번" %(word, n))
    cnt.append(n)
f.close()

import matplotlib.pyplot as plt
plt.rc("font", family = "Malgun Gothic")
plt.title("단어개수")
plt.xlabel("검색단어")
plt.ylabel("단어개수")
plt.bar(words, cnt)
plt.show()









































