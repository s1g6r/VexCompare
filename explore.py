import json

with open("data/matches.json") as f:
    data = json.load(f)

for match in data["data"]:
    for alliance in match["alliances"]:
        team_numbers = []
        for t in alliance["teams"]:
            team_numbers.append(t["team"]["name"])
        print(alliance["color"], match["round"], team_numbers, alliance["score"])

