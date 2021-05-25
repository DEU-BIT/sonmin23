y = int(input("몇줄?"))

for i in range(1, y+1):
    for j in range(i):
        print("*", end = "")
    print()
