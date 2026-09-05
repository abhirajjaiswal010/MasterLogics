'''
10. Take 5 numbers as input. If the user enters 0, skip that number
    using the continue statement. At the end, print the sum of all
    non-zero numbers entered.

Test Case:
Input:
Enter number: 10
Enter number: 0
Enter number: 20
Enter number: 5
Enter number: 0

Output:
Sum of non-zero numbers: 35
'''
sum=0
for i in range(5):
    n=int(input("Enter : "))
    if n==0:
        continue
    sum+=n

print(f"Sum Of non-zero num : {sum}")

