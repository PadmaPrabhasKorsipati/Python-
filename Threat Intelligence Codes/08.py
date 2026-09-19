f=open("scenario.csv")

next(f)


for x in f:

    src,dst,action=x.strip().split(",")

    if action=="block":
        print(f"{src}->{dst} : BLOCKED")

    else:
        print(f"{src}->{dst}:ALLOWED")

    

