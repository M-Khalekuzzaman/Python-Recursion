# Write a python program to solve the fibonicci sequence using recursion
def fibonicci(n) :
    if n == 1 or n == 2 :
        return 1
    else:
        return fibonicci(n-1) + fibonicci(n-2)

n = int(input("Enter your fibonicci number : "))
Fibonacci = fibonicci(n)
print("Fibonacci number is : ",Fibonacci)