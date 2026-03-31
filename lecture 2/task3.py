Gender = input("Enter your biological gender:").upper()

HB = float(input("enter your homoglobin level:"))

if Gender == "FEMALE":
    if HB <117:
        print("your homoglobin level is low.")
    elif HB <= 155:
        print("your homoglobin level is normal.")
    else:
        print("your homoglobin level is high.")
elif Gender == "MALE":
    if HB <134:
        print("your homoglobin level is high.")
    elif HB <= 167:
        print("Your homoglobin levedl is normal.")
    else:
        print("your homoglobin level is high.")
