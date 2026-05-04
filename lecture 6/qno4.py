def remove_odd(nums):
    new = []
    for n in nums:
        if n % 2 == 0:
            new.append(n)
    return new

nums = [1, 2, 3,4,5,6,7,8,9,10]

print(nums)
print(remove_odd(nums))