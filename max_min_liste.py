numbers = [3, 6, 2, 8, 4, 10]
maxi = numbers[0]

for number in numbers:
    if number > maxi:
        maxi = number

print(maxi)

mini = numbers[0]

for number in numbers:
    if number < mini:
        mini = number

print(mini)
