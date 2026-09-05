'''
8. Print the factorial of each number from 1 to n.

Test Case:
Input:
Enter n: 5

Output:
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
'''


n=int(input("Enter : "))

for i in range(1,n+1):
    p=1
    j=1
    while j<=i:
        p*=j
        j+=1
    print(f"{i}! -> {p}")
        