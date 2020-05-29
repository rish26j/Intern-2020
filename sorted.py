num = [3,7,5,2,7,9,5,4,6,]
print(sorted(num))
#However, sorted doesn't change num
print(num)

spotify = [
    {"Song1":"Title1","Playcount":33},
    {"Song2": "Title2", "Playcount": 88},
    {"Song3": "Title3", "Playcount": 56},
    {"Song4": "Title4", "Playcount": 21}
    ]
print(sorted(spotify,key = lambda x : x["Playcount"]))