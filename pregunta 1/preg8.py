#PREGUNTA 8
def fact(x):
    if x == 0 or x == 1:
        return 1
    else:
        c = 1
        for i in range(2, x + 1):
            c *= i
        return c
fact(x)
