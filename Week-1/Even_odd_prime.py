#Even/odd And prime number checker
num=int(input("enter any number of your choice : "))        
if(num%2==0):
    print("even number")
else:
    print("odd number")

if(num<=1):
    print("Prime number")
else:
    prime=True            
    for i in range(2,int(num**0.5)+1):
        if(num%i==0):
            prime=False
            break
    if prime:
        print("and number is prime") 
    else:
        print("and number is not prime")       