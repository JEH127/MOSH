letters = ["a", "b", "c", "d"]

matrix = [[0, 1], [2, 3]]
print(matrix)
zeros = [0] * 5
combined = zeros + letters
print(combined)

# 1ère manière
numbers_1 = list(range(20))
print(numbers_1)

# 2ème manière
numbers_2 = [i for i in range(20)]
print(numbers_2)

chars_1 = list("Hello World")
print(chars_1)

chars_2 = [i for i in "Hello World"]
print(chars_2)

letters[0] = "A"
print(letters)
print(letters[::2])

numbers_3 = list(range(20))
print(numbers_3[::-1])  # => reverse order

letters.insert(0, "-")
print(letters)
letters.pop(0)
print(letters)

print(letters.count("c"))

del letters[:2]
print(letters)

letters.clear()
print(letters)
