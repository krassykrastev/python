# You are a pro MOBA player, you are struggling to become а master of the Challenger tier.
# So, you carefully watch the statistics in the tier.
# You will receive several input lines in one of the following formats:
# "{player} -> {position} -> {skill}"
# "{player} vs {player}"
# The "player" and "position" are strings, and the given "skill" will be an integer number.
# You need to keep track of every player.
# When you receive a player with his position and skill, add him to the players' pool, if he isn`t present,
# else add his position and skill or update his skill, only if the current position skill is lower than the new value.
# If you receive "{player} vs {player}" and both players exist in the tier, they duel with the following rules:
# • If they got at least one position in common, the player with better total skill points wins and the other is demoted
# from the tier -> remove him.
# • If they have same total skill points at the same positions, the duel is tie and they both continue in the Season.
# • If they don`t have positions in common, the duel isn`t happening and both continue in the Season.
# You should end your program when you receive the command "Season end". At that point you should print the players,
# ordered by total skill in descending order, then ordered by player name in ascending order.
# For each player print their position and skill, ordered descending by skill, then ordered by position name in ascending order.
# Input / Constraints
# • The input comes in the form of commands in one of the formats specified above.
# • Player and position will always be one word string, containing no whitespaces.
# • Skill will be an integer in the range [0, 1000].
# • There will be no invalid input lines.
# • The program ends when you receive the command "Season end".
# Output
# • The output format for each player is:
# "{player}: {total_skills} skill"
# - {position1} <::> {skill}
# - {position2} <::> {skill}
# …
# - {positionN} <::> {skill}"
#
# Input1:
# Peter -> Adc -> 400
# George -> Jungle -> 300
# Simon -> Mid -> 200
# Simon -> Support -> 250
# Season end
#
# Output1:
# Simon: 450 skill
# - Support <::> 250
# - Mid <::> 200
# Peter: 400 skill
# - Adc <::> 400
# George: 300 skill
# - Jungle <::> 300
#
# Input2:
# Peter -> Adc -> 400
# Bush -> Tank -> 150
# Frank -> Mid -> 200
# Frank -> Support -> 250
# Frank -> Tank -> 250
# Peter vs Frank
# Frank vs Bush
# Frank vs Hide
# Season end
#
# Output2:
# Frank: 700 skill
# - Support <::> 250
# - Tank <::> 250
# - Mid <::> 200
# Peter: 400 skill
# - Adc <::> 400

players = {}

text_string = input()

while True:

    if "Season end" in text_string:
        break

    if "->" in text_string:
        player_name, position, skill = text_string.split(" -> ")
        skill = int(skill)

        if player_name not in players:
            players[player_name] = {position: skill}
        else:
            if position not in players[player_name]:
                players[player_name][position] = skill
            if players[player_name][position] < skill:
                players[player_name][position] = skill

    elif " vs " in text_string:
        first_player, second_player = text_string.split(" vs ")
        if first_player and second_player in players:
            for the_position in players[first_player]:
                if the_position in players[second_player]:
                    first_total_points = sum(players[first_player].values())
                    second_total_points = sum(players[second_player].values())
                    if first_total_points > second_total_points:
                        del players[second_player]
                    elif first_total_points < second_total_points:
                        del players[first_player]
                    break
    text_string = input()

best_player = {}

for name, position in players.items():
    best_player[name] = sum(position.values())

sorted_best_player = sorted(best_player.items(), key=lambda player: (-player[1], player[0]))

for player in sorted_best_player:
    skills = {}
    print(f"{player[0]}: {player[1]} skill")
    for skill in players[player[0]].items():
        skills[skill[0]] = skill[1]
    sorted_skills = sorted(skills.items(), key=lambda item: (-item[1], item[0]))
    for skill in sorted_skills:
        print(f'- {skill[0]} <::> {skill[1]}')