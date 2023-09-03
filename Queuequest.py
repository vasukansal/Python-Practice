import queue
# Given a positive number n, efficiently generate binary numbers between 1 and n using the queue
def decimalToBinary(n):
    return bin(n).replace("0b", "")

num=int(input("Enter the ending number - "))
q=queue.Queue ()
for i in range(1,num+1):
    q.put(i)
while(not q.empty()):
    print(decimalToBinary(q.get()))