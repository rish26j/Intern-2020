brands = {"Phone":"Samsung","Laptop":"Asus","Watch":"MI","Car":"Suzuki"}
print(brands)

brands["TV"]="Samsung"
print(brands)

is_true = "name" in brands
print(is_true)

for keys in brands:
    print(keys)

print("\n")

for value in brands.values():
    print(value)

print("\n")

print(brands.get("Laptop"))

print(brands.get("AC"))

brands.pop("Laptop")
print(brands)