c=input("Enter cipher:").upper()


freq={}

for ch in c:

    if ch.isalpha():
        freq[ch]=freq.get(ch,0)+1

freq=sorted(freq.items(),key=lambda x:x[1],reverse=True)

print("frequency:")

for ch,n in freq:
    print(ch,n)

print("\n The most frequent:"+freq[0][0])