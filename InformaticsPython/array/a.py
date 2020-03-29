a = int(input())
num_array =  [int(i) for i in input().split()]
for i in range(0,a):
    if (not(i % 2)):
        print(num_array[i],end=" ")