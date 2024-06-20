File="./sample.txt"

try:
    f=open(File,'r+')
    data=f.read()

    Content1=input("Enter the first to change - ")
    if(Content1 not in data):
        print(f"{Content1} is not present in the File")
    else:
        Final1=input("Enter the Final Content - ")
        data=data.replace(Content1,Final1)


    Content2=input("Enter the second to change - ")
    if(Content2 not in data):
        print(f"{Content2} is not present in file")
    else:
        Final2=input("Enter the Final Content - ")
        data=data.replace(Content2,Final2)


    Content3=input("Enter the third to change - ")
    if(Content3 not in data):
        print(f"{Content3} is not present in the file")
    else:
        Final3=input("Enter the Final Content - ")
        data=data.replace(Content3,Final3)

    f.seek(0)
    f.write(data)
    f.truncate()

    print("File changed")


except FileNotFoundError:
    print("File not Found")

