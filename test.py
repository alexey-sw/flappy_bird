from statistics import *
from random import randint
arr = []
for i in range(0,1000):
    arr.append(randint(-1000,1000))
print(mean(arr))