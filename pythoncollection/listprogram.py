#add a limit of numbers

limit=int(input("Enter limit:"))
lst=[]
for i in range(1,limit+1):
    lst.append(i)
print(lst)


even=[]
odd=[]
for num in lst:
    if(num%2==0):
        even.append(num)

    else:
        odd.append(num)
print(even)
print(odd)