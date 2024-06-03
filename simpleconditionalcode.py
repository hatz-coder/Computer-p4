fail = 0
passm = 0

for i in range(4):
    marks = int(input("enter your marks: "))
    if marks < 33:
        fail = fail + 1
    else:
        passm = passm + 1
print("The number of children that failed is: ", fail)
print("The number of children that passed is: ", passm)
