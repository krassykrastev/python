gradusi = float(input())
weather = ""

if 26 <= gradusi <= 35:
    weather = "Hot"

elif 20.1 <= gradusi <= 25.9:
    weather = "Warm"

elif 15 <= gradusi <= 20:
    weather = "Mild"

elif 12 <= gradusi <= 14.9:
    weather = "Cool"

elif 5 <= gradusi <= 11.9:
    weather = "Cold"

else:
    weather = "unknown"

print(weather)
