'''
Docstring for Phase01.Level05.05ArithmeticProgression
5. Take three numbers and check if they are in arithmetic progression.

   Test Cases:
   Input: 2 4 6
   Output: Arithmetic Progression

   Input: 10 7 4
   Output: Arithmetic Progression

   Input: 3 6 10
   Output: Not Arithmetic Progression

   Input: 5 5 5
   Output: Arithmetic Progression

'''
a,b,c=map(int,input("Enter Three Number : ").split())

if b-a==c-b:
    print("Arithmetic Progression")
else:
    print("Not ")