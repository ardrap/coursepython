#create a function to find factorial of a given number

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))