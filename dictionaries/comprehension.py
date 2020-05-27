info={"name":"Rishabh Jain","Age":"19","City":"Jaipur","College":"BITS Pilani"}

info_capital = {k.upper(): v.upper() for k,v in info.items()}

print(info_capital)

numbers={"one":1,"two":2,"three":3,"four":4}

numbers2={num:values**2 for num,values in numbers.items()}
print(numbers2)


num_list = [1,2,3,4,5]
print({num:("even" if num%2==0 else "odd") for num in range(1,11)})