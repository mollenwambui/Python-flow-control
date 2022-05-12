#skips  the remeinder of the current iteration and moves to  thee next iteration
x=1
y=50
while x<y:
    x+=1
    if x%5!=0:
        continue
    print(x) 