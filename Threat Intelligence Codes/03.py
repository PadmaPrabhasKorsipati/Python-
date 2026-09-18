p = input("Enter policy: ").lower()

req = ["scope", "roles", "enforcement", "review", "approval"]

for x in req:
    if x in p:
        print(x, "Present")
    else:
        print(x, "Missing")