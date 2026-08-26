n1=int(input("Enter The Num-1 : "))
n2=int(input("Enter The Num-2 : "))
n3=int(input("Enter The Num-3 : "))


if n1>n2 and n1>n3:
    print(f"{n1} is greater")
elif n2>n3 :
    print(f"{n2} is greater")
else:
    print(f"{n3} is greater")