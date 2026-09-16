c=input("Enter text:").upper()

A=[1,3,5,7,9,11,15,17,19,21,23,25]


for a in A:

    for b in range(26):


        for x in range(26):
            if(a*x)%26==1:
                inv=x
                break

        p=""

        for ch in c:
            if ch.isalpha():
                p+=chr((inv*(ord(ch)-65-b))%26+65)

            else:
                p+=ch

        print("a=",a," b=",b," :",p)