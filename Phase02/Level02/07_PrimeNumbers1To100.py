'''
07. Print Prime Numbers from 1 to 100

Question:
Write a program to print all prime numbers between 1 and 100.

A prime number is a number greater than 1 that has exactly
two factors: 1 and itself.

Test Case:

Input:
No input

Output:
2 3 5 7 11 13 17 19 23 29
31 37 41 43 47 53 59 61 67 71
73 79 83 89 97
'''


for i in range(2,101):

    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                
                break
        else:
            print(i,end=" ")
    

    