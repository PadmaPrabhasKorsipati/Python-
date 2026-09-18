f = open("scenario.csv")
data = f.readlines()

for row in data:
    print(row.strip())

f.close()