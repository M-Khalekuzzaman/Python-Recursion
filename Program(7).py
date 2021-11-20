# Write a python program to calculate the value of 'a' to the power 'b'
def value(a,b) :
    if  b == 0 :
        return 1
    elif a ==0 :
        return 0
    elif b == 1 :
        return a
    else:
        return pow(a,b)
print(value(3,4))