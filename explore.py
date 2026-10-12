import json

with open("data/matches.json") as f:
    data = json.load(f)

qual_count = 0

for match in data["data"]:
    if match["round"] == 2:
        qual_count += 1
        for alliance in match["alliances"]:
            team_numbers = []
            for t in alliance["teams"]:
                team_numbers.append(t["team"]["name"])
            print(alliance["color"], match["round"], team_numbers, alliance["score"])
print(qual_count)

