#NH 2nd mapping notes

numbers = [42, 67, 3456789, 4, 1, 1234, 465, 5678, 90]
"""divided = []

for num in numbers:
    divided.append(num/2)"""

"""def divide(number):
    return number/2"""

divided=list(map(lambda num: num/2, numbers))

for i, num in enumerate(numbers):
    print(f"{num} divided by 2 is {divided[i]}")