a = int(input())
for x in range(1, a + 1):
    if (not(a % x)):
        print(x,end=" ")