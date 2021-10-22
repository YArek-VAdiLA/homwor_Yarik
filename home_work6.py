slovo=input("ведите слово ")
print(slovo[0])
x=slovo[0]
x1=slovo
c=0
if x=="a" or x=="e" or x=="y" or x=="u" or x=="o":
 x1 = slovo + "way"
 print(x1)
elif slovo.isdigit():
    print("eror")
else:
    x1 = x1[1:]
    print(x1)
    x1 += x + "ay"
    print(x1)