def to_liters(g):
    return g * 3.785


while True:
    g = float(input("Gallons: "))

    if g < 0:
        break

    print("Liters:", to_liters(g))