import json

data = []
with open('data/Dota_2.jsonlines') as f:
    for line in f:
        data.append(json.loads(line))
        
reviews = list(map(lambda row: (row["review"], row["date_posted"]),data))
with open("data/dota2.csv", "w") as f:
    f.write("review;date_posted\n")
    for review,date in reviews:
        f.write("{0};{1}\n".format(review.replace(";",","),date))