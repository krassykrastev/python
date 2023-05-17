from math import ceil, floor
x_kv_m_loze = int(input())
y_grozde_1kv_m = float(input())
z_nujni_litri_vino = int(input())
broi_rabotnici = int(input())

total_grozde = x_kv_m_loze * y_grozde_1kv_m
vino = total_grozde * 0.4 / 2.5

if vino >= z_nujni_litri_vino:
    diff = vino - z_nujni_litri_vino
    print(f'Good harvest this year! Total wine: {vino:.0f} liters.')
    print(f'{ceil(diff):.0f} liters left -> {ceil(diff / broi_rabotnici):.0f} liters per person.')

else:
    diff = z_nujni_litri_vino - vino
    print(f'It will be a tough winter! More {floor(diff)} liters wine needed.')
