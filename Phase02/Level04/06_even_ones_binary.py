'''
6. Print all numbers from 1 to n whose binary representation
   contains an even number of 1s.

Test Case:
Input:
Enter n: 10

Binary representations:
1  -> 1       -> 1 one
2  -> 10      -> 1 one
3  -> 11      -> 2 ones
4  -> 100     -> 1 one
5  -> 101     -> 2 ones
6  -> 110     -> 2 ones
7  -> 111     -> 3 ones
8  -> 1000    -> 1 one
9  -> 1001    -> 2 ones
10 -> 1010    -> 2 ones

Output:
3 5 6 9 10
'''

n=int(input("Enter : "))
for i in range(1,n+1):
    # bin=''
    n=i
    oneCount=0
    while n>0:
        r=n%2 
        if r==1:
            oneCount+=1    
        # bin=str(r)+bin
        n//=2

    # print(oneCount,"->",bin)
    if oneCount%2==0:
        print(i)



