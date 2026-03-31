cabin_class = input("enter cabin class.") .upper()
if cabin_class == "LUX":
    print("upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("cabin above the car deck with window.")
elif cabin_class == "B":
    Print("window cabin above the car deck.")
elif cabin_class == "C":
    print("window cabin below the car deck.")
else:
    print("invalid cabin class")