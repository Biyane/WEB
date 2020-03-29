input = input()
a, b = map(int,input.split())
for x in range(int(a), int(b) + 1):
    if (not(x % 2)):
        print(x, end=" ")