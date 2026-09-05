'''
9. Find the sum of all odd digits and the sum of all even digits
   separately in a given number.

Test Case:
Input:
Enter number: 583921

Output:
Sum of odd digits: 18
Sum of even digits: 10
'''


n=int(input("Enter : "))

odd_sum=0
even_sum=0


while n>0:
    d=n%10
    if d%2==0:
        even_sum+=d
    else:
        odd_sum+=d
    n//=10

print(f"Sum of Odd Digits : {odd_sum}")
print(f"Sum of Even Digits : {even_sum}")