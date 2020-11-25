n=int(input("enter number"))
min=int(input("enter minimum"))
max=int(input("enter max"))

for i in range(1,(max+1)):
    if i**n in range(min,(max+1)):
        print(i,",",i,"^",n,"=",i**n)









