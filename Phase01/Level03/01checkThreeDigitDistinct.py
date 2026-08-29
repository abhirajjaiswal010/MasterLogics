'''
Question 1:

Take a 3-digit number and check if all digits are distinct. mtlb alag alg

Example 1:
Input: 123
Output: All digits are distinct

Example 2:
Input: 121
Output: Digits are not distinct
'''

n=input("Enter The Number : ")
found=True #distinct hai 

for i in range(len(n)):
    count=0
    for j in range(i+1,len(n)):
        if n[i]==n[j]:
            
            count+=1
    
    if count!=0:
        found=False # not distinct
        break

if found:
    print("distinct")
else:
    print("not distinct")


#* approach by set


if len(set(n))==len(n):
    print("distinct")
else:
    print("not distinct")

#* approach by seen

seen=""

for i in n:
    if i not in seen:
        seen+=i


if len(seen)==len(n):
    print("distinct")
else:
    print("not distinct")


    




