import numpy as np
call = 15



add = []
nm = 0

while call > nm:
    lit = []
    n = 0

    while call > n:
        try:
            n += 1
            lit.append(n)
            add.append(lit)
            nm += 1
        except:
            break
    
    n = 0
   


pizza = np.array(add)






for i in range(7):
  for j in range(14,6-i,-1):
    pizza[i][j] = 0


for p in range(7,15): #아래 조각 완성
    for q in range(p-1,15):
      pizza[p][q] = 0
      # print(p)


#----------------------------------------------------------------
# for i in range(15):
#   for j in range(14 - (i+1)):
#     pizza[i][j] = 0

# for p in range(7,0,-1):
#   for q in range(14,p-1,-1):
#     pizza[p][q] = 0

print(pizza)