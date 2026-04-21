smallest = 10
largest = 15

while True:
    user_input = input("Enter a number: ").strip()# remove spaces
    if user_input == "":
        break

    number = int(user_input)


    if  number < smallest:
        smallest = number
    if number > largest:
        largest = number


if smallest is not None and largest is not None:
    print("The smallest number entered is:", smallest)
    print("The largest number entered is:", largest)
else:
    print("No numbers were entered.")
