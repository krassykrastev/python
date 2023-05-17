best_player_score = 0
current_player_score = 0
goals = 0
best_player_name = ''

while current_player_score < 10:
    current_player_name = input()
    if current_player_name == 'END':
        break
    else:
        current_player_score = int(input())

    if current_player_score > best_player_score:
        best_player_score = current_player_score
        best_player_name = current_player_name

#    if current_player_score >= 3:
#        goals = current_player_score

print(f'{best_player_name} is the best player!')
if best_player_score >= 3:
    print(f'He has scored {best_player_score} goals and made a hat-trick !!!')
else:
    print(f'He has scored {best_player_score} goals.')
