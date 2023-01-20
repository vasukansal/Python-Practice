def fibonacci(n):
    if n==0:
        return 0
    elif n==1 :
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

a=int(input("Enter no. to get its fibonacci series - "))
print(fibonacci(a))