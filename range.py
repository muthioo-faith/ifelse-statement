import numbers


n=int(input("Enter any number \n"))
if n%2==0 and n in range(2,5):
    print("Not weird")
elif n%2==0 and n in range(6,20):
    print("weird")
elif n%2==0 and n>20:
    print("Not weird") 
elif n%2!=0:
    print("Weird")   


# given a number y solve the following
# 1,if y is a multiple of 3 print fizz
# if y is multiple of 5 print buzz
# if y is multiple of 3 and 5 print fizzbuzz
# rnge 1-100  
# 

for y in range(1,101):
     if y%3==0 and y%5==0 :
        print("FizzBuzz")  
     elif y%3==0:
        print("Fizz")
     elif y%5==0:
        print("Buzz") 
     else:
        print(y)