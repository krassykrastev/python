number = int(input())
bonus = 0

if number <= 100:
    bonus += 5 #съкратено изписване на израза bonus = bonus + 5

elif number > 1000:
    bonus += number * 0.1

else:
    bonus += number * 0.2

if number % 2 == 0:
    bonus += 1 # за четни числа +1 бонус точка

elif number % 10 == 5: # с тази формула намираме в десетична бройна система всички числа, които завършват на 5
    bonus += 2 # ако числото завършва на 5 €2 бонус точки

print(bonus)
print(number + bonus)
