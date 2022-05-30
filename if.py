x=range(21)
for y in x:
    if y%3==0:
        print(f"{y} weird")
    elif y%2 :
        print(f"{y}not  weird")
    elif y%6==20:
        print(f"{y} weird")
    else:
        print(f"{y} if 20 =>not weird")