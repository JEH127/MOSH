weight = input("Weight: ")
type_weight = input("(L)bs or (K)g: ")

if type_weight.upper() == 'K':
    weight_pounds = int(weight) / 0.45
    print(f"You are {weight_pounds} pounds")
elif type_weight.upper() == 'L':
    weight_kg = int(weight) * 0.45
    print(f"You are {weight_kg} kg")
