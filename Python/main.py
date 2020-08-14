import math

sum = 0
for i in range(1,1000000000):
    sum+=math.sqrt((1/(i**2))*6)

print(sum)