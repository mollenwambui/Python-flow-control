#stops a while loop even if the set condition is true.
x=1
y=10
while x <=y:
    print(x)
    x+=1
    if x==5:
     break   