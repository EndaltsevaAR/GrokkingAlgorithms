def fact(x):  # example: find factorial 4! = 4*3*2*1
    if x == 1:
        return x
    else:
        return x * fact(x - 1)


print(fact(4))
