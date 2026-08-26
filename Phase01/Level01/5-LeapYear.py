n=int(input("Enter The Year : "))

if n%4==0:
    if n%100==0 and n%400==0:
        print("Year is Century Leap Year")
    else:
        print("Year is Leap year")
else:
    print("Year is not Leap year")