"""
03. PRINT ODD NUMBERS

Write a Python program to print all odd numbers between 1 and 100.
"""

for i in range(1,101):
    if i%2!=0:
        if i<100:
            print(i,end=",")
        else:
        
            print(i,end=" ")