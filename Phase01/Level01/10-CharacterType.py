# 10. Take a character and check whether it’s uppercase, lowercase, a digit, or a special
# character.


n=input("Enter The String ")

u=0
l=0
d=0
s=0


for i in n:
    if 'a'<=i<='z':
        l=1
    elif  'A'<=i<='Z':
        u=1
    elif '0'<=i<='1':
        d=1
    else:
        s=1

if u==1 and l==1 and d==1 and s==1:
    print("all have")
else:
    print("not have")