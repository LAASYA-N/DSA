# 1.solid square patttern
#     * * * * *
#     * * * * *
#     * * * * *
#     * * * * *
#     * * * * *

for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()


print("---------")

# 2.Left  half pyramid pattern
#  *
#  * *
#  * * *
#  * * * *
#  * * * * *

n=5
for i in range(n):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

print("---------")

# 3.Left half period(same number)
#  1
#  2 2
#  3 3 3
#  4 4 4 4
#  5 5 5 5 5

for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print()  


print("---------")  


# Left half pyramid(Increasing numbers)

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()  


