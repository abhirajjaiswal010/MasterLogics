n=input("Enter The String ")

vowCount=0
conCount=0

for i in n:

    if i in  "aeiou" or i in "AEIOU":
        vowCount+=1
    else:
        conCount+=1

print(f"vowel count  : {vowCount}")
print(f"Consonant count  : {conCount}")
