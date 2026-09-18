host = input("Enter target: ")

ports = [21, 22, 23, 80, 443]
open_ports = [22, 80, 443]

for p in ports:
    if p in open_ports:
        print(p, "OPEN")
    else:
        print(p, "CLOSED")