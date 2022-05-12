x=range(30)
for y in x:
    if y%4==0 and y%5==0:
        print(f"{y} is divisible by both 4 and 5")
    elif y%4==0:
        print(f"{y} is divisible by 4")
    elif y%5==0:
        print(f"{y} is divisible by 5")
    elif y%7==0:
        print(f"{y} is divisible b by 7")   
    else:
        print(f"{y} not divisible by 4,5,7")     
