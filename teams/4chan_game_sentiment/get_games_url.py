
fn = open("game_list").read()
for line in fn:
    url = "http://www.metacritic.com/game/xbox-360/"+line
