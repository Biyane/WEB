import math
a = int(input())
cnt = 0
if (a < 10):
    for x in range(1, 11):
        if (a % x == 0):
            cnt+=1
else:
    for x in range(1, int(math.sqrt(a)) + 1):
        if (not(a % x)):
            cnt+=2
print(cnt)

