print("======================================")
matriksA = ([1,2,3],
            [3,4,5],
            [8,7,6])

matriksB = ([2,5,6],
            [7,8,9],
            [3,5,7])
for x in range(0, len(matriksA)):
    print()
    for y in range(0, len(matriksA[0])):
        print(matriksA[x][y], end="  ")
print()
print("========================================")