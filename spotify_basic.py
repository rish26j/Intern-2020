spotify = {"PLaylist":"Rock Classics",
           "Author":"Rishabh Jain",
           "Date Created": "29/02/2020",
           "Songs":[
                {"Title1":"Comfortably Numb","Artist":"Pink Floyd","Duration":6.22},
                {"Title2":"Shoot to Thrill","Artist":"AC/DC","Duration":5.17},
                {"Title3":"Bohemian Rhapsody","Artist":"Queen","Duration":5.54}]
           }
print(spotify)

total_time=0
for time in spotify["Songs"]:
    total_time+=time["Duration"]

print(total_time)