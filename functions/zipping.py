num = [1,2,3,4,5,6,7]
num1= [1,4,9,16,25,36,49]

print(list(zip(num,num1)))


midterms = [45,42,49]
finals = [93,98,90]
names = ["AJ","AK","AR"]

final_score = {t[0]:max(t[1],t[2]) for t in zip(names,midterms,finals)}
print(final_score)
