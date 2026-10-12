import json

with open("data/matches.json") as f:
    data = json.load(f)

records = {}

for match in data["data"]:
    if match["round"] == 2:

        # STEP 1: get each alliance's teams and score
        for alliance in match["alliances"]:
            team_numbers = []
            for t in alliance["teams"]:
                team_numbers.append(t["team"]["name"])

            if alliance["color"] == "red":
                red_teams = team_numbers
                red_score = alliance["score"]
            else:
                blue_teams = team_numbers
                blue_score = alliance["score"]

        if red_score > blue_score:
            red_result = "W"
            blue_result = "L"
        elif blue_score > red_score:
            blue_result = "W"
            red_result = "L"
        else:
            red_result = "T"
            blue_result = "T"

        for team in red_teams:
            if team not in records:
                records[team] = {"W": 0, "L": 0, "T": 0}
            records[team][red_result] += 1

        for team in blue_teams:
            if team not in records:
                records[team] = {"W": 0, "L": 0, "T": 0}
            records[team][blue_result] += 1

for team in records:
    r = records[team]
    print(team, f"{r['W']}-{r['L']}-{r['T']}")