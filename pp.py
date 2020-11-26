#startriangle
#for row in range(1,5):
#   for col in range(1,8):
#       if row==4 or row+col==5 or col-row==3:
#         print("*",end="\t")
#       else:
#         print(end="\t")
#   print()


#123..123..123
#for row in range(1,4):
#   for col in range(1,4):
#       print(col,end="\t")
#   print()


#starpyramid
#for row in range(0,5):
#   for col in range(0,row):
#       print("*",end="\t")
#   print()

#1..22...333...4444
#for row in range(1,5):
#   for col in range(1,row+1):
#       print(row,end="\t")
#   print()

#1..12...123...1234..
#for row in range(1,5):
#   for col in range(1,row+1):
#       print(col,end="\t")
#   print()


#prime
#num=int(input("Enter a number:"))
#flag=0
#for i in range(2,num):
#   if(num%i==0):
#       flag+=1
#       break
#if(flag==0 or num==2):
#    print("prime number")
#else:
#   print("not a prime number")

#palindrome
a=int(input("enter:"))
temp=a
reverse=0
while a!=0:
    dig=a%10
    reverse=reverse*10+dig
    a=a//10
print(reverse)
print(a)
if(reverse==temp):
    print("pal")
else:
    print("not pal")