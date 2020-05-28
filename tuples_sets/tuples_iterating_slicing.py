months = ("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")

for month in months:
    print(month)

print("\n")

i=len(months)-1
while i>=0:
    print(months[i])
    i-=1

print(months.count("Jan"))

print(months.index("Jul"))

print(months[2:9:])
