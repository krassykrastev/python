price_skumria_kg = float(input())
price_caca_kg = float(input())
kg_palamud = float(input())
kg_safrid = float(input())
kg_midi = int(input())
price_midi_kg = 7.50

price_palamud_kg = price_skumria_kg + (price_skumria_kg * 0.60)
price_safrid_kg = price_caca_kg + (price_caca_kg * 0.80)

total_price = price_palamud_kg * kg_palamud + price_safrid_kg * kg_safrid + price_midi_kg * kg_midi

print(f'{total_price:.2f}')
