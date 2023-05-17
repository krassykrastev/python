number_of_kilometers = int(input())
time_of_transport = input()

taxi_price_per_km = 0

bus_price_per_km = 0.09
train_price_per_km = 0.06
mode_of_transport = ""
price = 0

if time_of_transport == "day":
    taxi_price_km = 0.79

elif time_of_transport == "night":
    taxi_price_km = 0.90

if number_of_kilometers < 20: #taxi mode of transport
    price = 0.70 + taxi_price_km * number_of_kilometers

elif 20 <= number_of_kilometers < 100: #bus mode of transport
    price = 0.09 * number_of_kilometers

elif number_of_kilometers >= 100: #train mode of transport
    price = 0.06 * number_of_kilometers

print(f'{price:.2f}')

