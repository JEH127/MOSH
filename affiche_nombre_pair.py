count = 0
for i in range(2, 10):
    if i % 2 == 0:
        count += 1
        print(i)
    else:
        continue

print(f"We have {count} even numbers")
