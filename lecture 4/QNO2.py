nums = []

while True:
    n = input("Number: ")
    if n == "":
        break
    nums.append(int(n))

nums.sort(reverse=True)
print(nums[:5])