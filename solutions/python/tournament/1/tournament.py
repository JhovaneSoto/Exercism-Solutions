def tally(rows):
    out=["Team                           | MP |  W |  D |  L |  P"]
    teams={}
    for row in rows:
        team_a,team_b,result=row.split(";")
        if team_a not in teams.keys():
            teams[team_a]={
                "MP":0,
                "W":0,
                "D":0,
                "L":0,
                "P":0
            }
        if team_b not in teams.keys():
            teams[team_b]={
                "MP":0,
                "W":0,
                "D":0,
                "L":0,
                "P":0
            }

        teams[team_a]["MP"]+=1
        teams[team_b]["MP"]+=1
        if result=="win":
            teams[team_a]["W"]+=1
            teams[team_a]["P"]+=3
            teams[team_b]["L"]+=1
        if result=="draw":
            teams[team_a]["D"]+=1
            teams[team_a]["P"]+=1
            teams[team_b]["D"]+=1
            teams[team_b]["P"]+=1
        if result=="loss":
            teams[team_a]["L"]+=1
            teams[team_b]["W"]+=1
            teams[team_b]["P"]+=3
            
    teams=dict(sorted(teams.items(),key=lambda item: item[0]))
    
    teams=dict(sorted(teams.items(),key=lambda item: (item[1]["P"]),reverse=True))
    for team in teams.keys():
        out.append(f"{team:<30} | {teams[team]['MP']:2} | {teams[team]['W']:2} | {teams[team]['D']:2} | {teams[team]['L']:2} | {teams[team]['P']:2}")
    print(out)
    return out