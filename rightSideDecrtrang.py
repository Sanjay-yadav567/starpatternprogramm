n = 5

for i in range(n):
    for j in range(i+1): #Here we use this loop for increasing space order
        print(" ",end=' ')

    for j in range(i,n): #Here we use this loop for decreasing Star order
        print('*',end=' ')
    print()