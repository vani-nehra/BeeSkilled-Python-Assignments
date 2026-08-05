# 1. Temperature Converter Celcius -> Fahrenheit
def temp_converter(c):
    return(c*9/5)+32

choice=int(input("Enter temperature in Celcius : "))
print(temp_converter(choice))

#Student Grade Calculator
marks1=int(input("Enter marks in subject 1 : "))
marks2=int(input("Enter marks in subject 2 : "))
marks3=int(input("Enter marks in subject 3 : "))
marks4=int(input("Enter marks in subject 4 : "))
marks5=int(input("Enter marks in subject 5 : "))
avg = (marks1 + marks2 + marks3 + marks4 + marks5)/5
print("average : "+avg)
if(avg>=90):
    print("grade : A+")
elif(avg>=80):
    print("grade : A")
elif(avg>=70):
    print("grade : B")
elif(avg>=60):
    print("grade : C")
elif(avg>=50):
    print("grade : D")
elif(avg>=40):
    print("grade : E")
else:
    print("Fail")