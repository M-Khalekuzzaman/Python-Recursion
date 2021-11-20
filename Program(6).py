# Write a python program to calculate the harmonic sum  of (n-1)
def series(n) :
    if n < 2 :
        return 1
    else :
        return 1 / n  + series(n-1)
print(series(7))
print(series(4))


