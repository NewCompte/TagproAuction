import json


## Edit these then run the script to generate the data you need
captains = [('eagles.', "Capitalists", "Central"),
			('Bull', "Cyber Ballies", "Pacific"),

		]


starting_money = 100
team_size = 4

keepers = False
nominations = [{"name" : "nextInOrder", "nextorder" : 0}]
team_names = []
keepers = []
teams = []
for index, data in enumerate(captains):
	captain, team_name, division = data
	nominations.append({"name" : captain, "rosterfull" : False, "order" : -1})
	team_names.append({"teamname":team_name, "division" : division, "money" : starting_money, "keepermoney":0, "captain":captain, "numrosterspots":team_size, "count":1, "order":index})
	teams.append({"name" : captain, "captain":True, "order" : 1, "cost" : 0, "division" : division, "teamname" : team_name })
	for x in range(2, team_size+1):
		teams.append({"name":"", "order" : x, "cost" : 0, "division" : division, "teamname" : team_name })
	keepers.append({"captain" : captain, "keepers":[]})

division_names = set(c[2] for c in captains)
divisions = []
for index, division in enumerate(division_names):
	divisions.append({"division": division, "order":index})

with open("./private/nominations.json", "wb") as f:
	f.write(json.dumps(nominations))
with open("./private/teamnames.json", "wb") as f:
	f.write(json.dumps(team_names))
with open("./private/divisions.json", "wb") as f:
	f.write(json.dumps(divisions))
with open("./private/teams.json", "wb") as f:
	f.write(json.dumps(teams))
with open("./private/keepers.json", "wb") as f:
	f.write(json.dumps(keepers))
