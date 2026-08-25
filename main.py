#Take input
print("Half Pyramid Pattern of Stars (*):")
n = int(input("Enter the number of rows:"))
#Outer loop to handle number of columns
for i in range(n):
    for j in range(i+1):
        #display result
        print("*", end="")
    print()