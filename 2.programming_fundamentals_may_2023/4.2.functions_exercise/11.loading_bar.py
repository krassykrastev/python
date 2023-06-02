def loading_bar(some_number):
    if some_number == 100:
        return '100% Complete!\n [%%%%%%%%%%]'
    loaded_percents = some_number // 10
    return f"{some_number}% [{'%' * loaded_percents}{'.' * (10 - loaded_percents)}]\nStill loading..."


number = int(input())
print(loading_bar(number))