def sumDigits(n) :
    if n == 0 :
        return 0
    else:
        return (n % 10) + sumDigits(int(n / 10))

n =int(input("ENter your sum digits : "))
number = sumDigits(n)
print("Integer number is :",number)
