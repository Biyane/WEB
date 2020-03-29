import math
a = int(input())
b = int(input())
for x in range(a, b + 1):
    if (math.sqrt(x) - math.floor(math.sqrt(x)) == 0):
        print(x,end=" ")