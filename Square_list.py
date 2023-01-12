while(1>0):
    print("1. Square list from 0 to 'n'\n2. Square list between 'n1' and 'n2'\n3. Exit")
    ch=int(input("Enter choice 1 or 2 - "))
    if(ch==3):
        break
    elif(ch==1):
        n=int(input("Enter the number you want squares till - "))
        lst=[i*i for i in range(n+1)]
        print("")
        print(lst)
        print("")
    elif(ch==2):
        n1=int(input("Enter the starting number - "))
        n2=int(input("Enter the number you want squares till - "))
        list=[i*i for i in range(n1,n2+1)]
        print("")
        print(list)
        print("")
    else:
        print("\n!!! invalid choice entered !!!\n")
print("\nBYEE :)\n")