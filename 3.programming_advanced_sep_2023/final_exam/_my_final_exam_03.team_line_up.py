# Uniting nations through teamwork and excellence.
# Embracing diversity, forging victory.
# Write a function called team_lineup that receives information about certain football players and their countries and
# returns a sorted result. The function will receive a tuple of key-value pairs as arguments. The arguments will be
# passed as follows:
# •	The following arguments will be the tuples with two elements - the first one is the player’s name (string), and the
# second one is the county’s name (string).
# First, you need to sort the given information as stated below:
# •	Sort the data by the number of players per country (descending);
# •	If the player count is the same in two or more countries, sort the data by country name (alphabetically).
# In the end, return the output as described below.
# Note: Submit only the function in the judge system
# Input
# •	There will be no input from the console, just parameters passed to your function.
# Output
# •	The output should look like this:
#    "{country_name}:"
#    "  -{player1}"
#    "  -{player2}"
#    "  -{playerN}"
# * Please note that there are exactly two intervals before the player’s name.
# Constraints
# •	Each tuple given will always contain the player’s name with its national country.
# •	You will NOT receive the same player in two or more different countries.
#
# Example1:
# print(team_lineup(
#    ("Harry Kane", "England"),
#    ("Manuel Neuer", "Germany"),
#    ("Raheem Sterling", "England"),
#    ("Toni Kroos", "Germany"),
#    ("Cristiano Ronaldo", "Portugal"),
#    ("Thomas Muller", "Germany")))
#
# Output1:
# Germany:
#   -Manuel Neuer
#   -Toni Kroos
#   -Thomas Muller
# England:
#   -Harry Kane
#   -Raheem Sterling
# Portugal:
#   -Cristiano Ronaldo
#
# Example2:
# print(team_lineup(
#    ("Lionel Messi", "Argentina"),
#    ("Neymar", "Brazil"),
#    ("Cristiano Ronaldo", "Portugal"),
#    ("Harry Kane", "England"),
#    ("Kylian Mbappe", "France"),
#    ("Raheem Sterling", "England")))
#
# Output2:
# England:
#   -Harry Kane
#   -Raheem Sterling
# Argentina:
#   -Lionel Messi
# Brazil:
#   -Neymar
# France:
#   -Kylian Mbappe
# Portugal:
#   -Cristiano Ronaldo
#
# Example3:
# print(team_lineup(
#    ("Harry Kane", "England"),
#    ("Manuel Neuer", "Germany"),
#    ("Raheem Sterling", "England"),
#    ("Toni Kroos", "Germany"),
#    ("Cristiano Ronaldo", "Portugal"),
#    ("Thomas Muller", "Germany"),
#    ("Bruno Fernandes", "Portugal"),
#    ("Bernardo Silva", "Portugal"),
#    ("Harry Maguire", "England")))
#
# Output3:
# England:
#   -Harry Kane
#   -Raheem Sterling
#   -Harry Maguire
# Germany:
#   -Manuel Neuer
#   -Toni Kroos
#   -Thomas Muller
# Portugal:
#   -Cristiano Ronaldo
#   -Bruno Fernandes
#   -Bernardo Silva


def team_lineup(*args):
    players_by_country = {}
    for player, country in args:
        if country not in players_by_country:
            players_by_country[country] = [player]
        else:
            players_by_country[country].append(player)

    sorted_countries = sorted(players_by_country.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ""
    for country, players in sorted_countries:
        result += f"{country}:\n"
        for player in players:
            result += f"  -{player}\n"

    return result


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))

print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))

print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))
