##import numpy as np
##
##a = ['1','2','3','4']
##
##b = np.array(a)
##c = np.array(a, dtype = int)
##
##print(b)
##print(c)



##import numpy as np
##
##c = np.arange(0,10,2)
##print(c)


##
##a = []
##
##for i in range(0,10,2) :
##    a.append(i)
##
##print(a)
##
##import numpy as np
##a = np.random.random()
##b = np.random.random(5)
##c = np.random.randint(1,101)
##d = np.random.randint(1,101,5)
##
##print(a)
##print(b)
##print(c)
##print(d)
##


import random
dice = []

for i in range(10) :
    dice.append(random.randint(1,6))
print(dice)






import csv
import numpy as np
import matplotlib.pyplot as plt

f = open("class2.csv", encoding = "euc-kr")
data = csv.reader(f)

h = next(data)
w = next(data)

h = np.array(h[2:], dtype = int)
w = np.array(w[2:], dtype = int)

for row in data :
    if '키' in row[1]:
        h = np.concatenate((h,np.array(row[2:], dtype = int)), axis = None)
    if '몸무게' in row[1] :
        w = np.concatenate((w, np.array(row[2:], dtype = int) ), axis = None)

f.close()
plt.scatter(h,w,c = w,cmap = 'jet')
plt.colorbar()
plt.show()




##import numpy as np
##import matplotlib.pyplot as plt
##x = np.random.randint(10,100,200)
##y = np.random.randint(10,100,200)
##size = np.random.random(200) * 100
##plt.scatter(x,y,s = size, c = y, cmap = 'jet', alpha = 0.7)
##plt.colorbar()
##plt.show()
