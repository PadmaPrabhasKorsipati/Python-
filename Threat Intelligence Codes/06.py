url=input("Enter the URL:")

score=0


if any(x in  url for x in ["login","verify","free","update","secure"]):
    score+=1

host=url.split("/")[2] if "//" in url else url

if host.replace(".","").isdigit():
    score+=1


if host.count(".") >3:
    score+=1


print("Phishing URL" if score>=2 else "Safe")
