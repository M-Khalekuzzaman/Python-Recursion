# Write a python program to calculate the sum of the positive integer n + (n-2) + (n-4) + ....
def sum_series(n) :
    if n < 1 :
        return  0
    else:
        return n + sum_series(n-2)

n = int(input("Enter your last number : "))
sum = sum_series(n)
print("Total sum is : ",sum)