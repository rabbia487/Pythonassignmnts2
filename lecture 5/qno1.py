seasons = ("Winter", "Spring", "Summer", "Autumn")

month = int(input("Enter month number: "))

if month in (12, 1, 2):
    print(seasons[0])
elif month in (3, 4, 5):
    print(seasons[1])
elif month in (6, 7, 8):
    print(seasons[2])
else:
    print(seasons[3])