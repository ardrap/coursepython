lst=[9,8,7,6,4,3,2]
out=[]
for num in lst:
    if(num>5):
      out.append(num+1)
    else:
      out.append(num-1)
print(out)