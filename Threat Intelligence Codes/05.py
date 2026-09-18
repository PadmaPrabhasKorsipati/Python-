s=input("Enter report and audiences:").lower()

if any(x in s for x in ["business","executives","long-term","management","stake-holders"]):
    print("Strategical Intelligence")

elif any(x in s for x in ["tactics","ongoing","techniques","architects","attack methods"]):
    print("Tactical Intelligence")

elif any(x in s for x in ["present","soc","analyst","alert","incident","ip","ioc"]):
    print("Operational Intelligence")

else:
    print("Unknown Intelligence")


