deposit_sum = float(input())
months = int(input())
year_interest_percent = float(input()) / 100

# сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)

final_sum = deposit_sum + months * ((deposit_sum * year_interest_percent) / 12)

print(final_sum)
