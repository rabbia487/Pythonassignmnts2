smallest = None
largest = None

while True:
    user_input = input("Enter a number: ") .strip()# remove spaces
    if user_input == "":
        break


    number = int(user_input)


    if smallest is None or number < smallest:
        smallest = number
    if largest is None or number > largest:
        largest = number


if smallest is not None and largest is not None:
    print("The smallest number entered is:", smallest)
    print("The largest number entered is:", largest)
else:
    print("No numbers were entered.")
