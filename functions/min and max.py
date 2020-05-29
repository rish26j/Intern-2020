spotify = [
    {"Song": "Title1","Playcount":33},
    {"Song": "Title2", "Playcount": 88},
    {"Song": "Title3", "Playcount": 56},
    {"Song": "Title4", "Playcount": 21}
    ]

least_plays = min(spotify, key = lambda s : s["Playcount"])["Song"]
print(least_plays)

cities = ["Jaipur","Delhi","Bangalore","Mumbai","Thiruvananthpuram"]
long_name = max(cities, key = lambda x : len(x))
print(long_name)