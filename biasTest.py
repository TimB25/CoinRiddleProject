import random
listBias = {0,1}
i = 9999
while(i > 0):
    listBias.append(random.getrandbits(1))
    i -=1

a = 0
b = 0

for y in range(len(listBias)):
    if(listBias[y] == 1):
        a += 1
    if(listBias[y] == 0):
        b += 1

print(a)
print(b)