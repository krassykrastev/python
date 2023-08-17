# Create a program that manages battles. You need to keep information about people, the health and energy they have.
# You will be receiving lines with commands until you receive the "Results" command. There are three possible commands:
# •	"Add:{personName}:{health}:{energy}":
# o	Add the person, his/her health and energy to your records. If person with the given name already exists, just increase the health of the person with the current one that is given.
# •	"Attack:{attackerName}:{defenderName}:{damage}":
# o	Check if both people exist and if they do, reduce the defender’s health with the damage given. If the defender’s health reaches 0 or less, the person is disqualified, and you need to remove him/her from your records and print the following message:
# 	"{defenderName} was disqualified!"
# o	You also have to reduce the attacker’s energy by 1. If it reaches 0, he/she is disqualified, and you need to remove him/her from your records and print the following message:
# 	"{attackerName} was disqualified!"
# •	"Delete:{username}":
# o	Delete all records of the given user, if he exists. If "All" is given as username - delete all records you have.
# In the end, you have to print the count of people left, each person with his/her health and energy sorted in descending order by the health and then by their name in ascending order in the following format:
# People count: {count}
# {personName} - {health} - {energy}
# {personName} - {health} - {energy}
# Input
# •	You will be receiving lines until you receive the "Results" command.
# •	The health is an integer number in the range [1...100000].
# •	The energy is an integer number in the range [1...100].
# •	The input will always be valid.
# Output
# •	Print the appropriate message after the "Attack" command, if someone is disqualified.
# •	Print the people with their health and energy in the format described above.
#
# Input1:
# Add:Mark:1000:5
# Add:Clark:1000:3
# Attack:Clark:Mark:500
# Add:Allison:2500:5
# Attack:Clark:Mark:300
# Add:Charlie:4000:10
# Attack:Clark:Mark:500
# Results
#
# Output1:
# Mark was disqualified!
# Clark was disqualified!
# People count: 2
# Charlie - 4000 - 10
# Allison - 2500 - 5
#
# Input2:
# Add:Bonnie:3000:5
# Add:Kent:10000:10
# Add:Johny:4000:10
# Attack:Johny:Bonnie:400
# Add:Chicken:1000:1
# Add:Rabbit:3000:5
# Add:Buggy:1259:10
# Delete:Kent
# Attack:Chicken:Rabbit:1000
# Results
#
# Output2:
# Chicken was disqualified!
# People count: 4
# Johny - 4000 - 9
# Bonnie - 2600 - 5
# Rabbit - 2000 - 5
# Buggy - 1259 - 10
#
# Input3:
# Add:Bonnie:3000:5
# Add:Johny:4000:10
# Delete:All
# Add:Bonnie:3333:3
# Results
#
# Output3:
# People count: 1
# Bonnie - 3333 - 3

command_line = input()
person_records = {}
while command_line != "Results":
    args = command_line.split(":")
    command = args[0]
    if command == "Add":
        person = args[1]
        health = int(args[2])
        energy = int(args[3])

        if person not in person_records:
            person_records[person] = [0, 0]
            person_records[person][0] += health
            person_records[person][1] += energy
        else:
            person_records[person][0] += health

    elif command == "Attack":
        attacker = args[1]
        defender = args[2]
        damage = int(args[3])
        if attacker and defender in person_records:
            person_records[defender][0] -= damage
            if person_records[defender][0] <= 0:
                print(f'{defender} was disqualified!')
                del person_records[defender]

            person_records[attacker][1] -= 1
            if person_records[attacker][1] <= 0:
                print(f'{attacker} was disqualified!')
                del person_records[attacker]
    elif command == "Delete":
        person = args[1]
        if person in person_records:
            del person_records[person]
        elif person == "All":
            person_records.clear()
    command_line = input()

print(f'People count: {len(person_records)}')
person_records = dict(sorted(person_records.items(), key=lambda x: (-x[1][0], x[0])))
for key, value in person_records.items():
    print(f'{key} - {value[0]} - {value[1]}')