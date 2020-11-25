#factorial

#def fact(n):
#    if n==0:
 #       return 1
 #   else:
#        return n*fact(n-1)
#n=int(input("enter a number:"))

#print(fact(n))






num=int(input("enter the number:"))
fact=1
if num==0: #1
    print(1)
elif num<0:#1
    print("invalid")
else:#1
    for i in range(1,num+1):
        fact=fact*i
    print(fact)
