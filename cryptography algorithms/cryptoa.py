p=input("Cipher").upper()


A=[1,3,5,7,9,11,15,17,19,21,23,25]

for a in A:

    for b in range(26):

        for x in range(26):
            if (a*x)%26==1:
                inv=x
                break


        c=""


        for ch in p:

            if ch.isalpha():
                c+=chr((inv*(ord(ch)-65-b))%26+65)

            else:
                c+=ch

        print("a=",a,"b=",b,":",c)


