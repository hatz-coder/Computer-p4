def Unknown(x, y):
    if x < y:
        print(x + y)
        return Unknown(x + 1, y) * 2
    else:
        if x == y:
            return 1
        else:
            print(x + y)
            return Unknown(x - 1, y) // 2


print(Unknown(10, 15))
Unknown(10, 15)
print(Unknown(10, 10))
print(Unknown(15, 10))
