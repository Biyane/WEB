import sys
a = int(input())
for x in range(2, a + 1):
    if (not(a % x)):
        print(x)
        sys.exit()