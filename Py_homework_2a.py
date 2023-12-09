age = int(input("Enter your age: "))

if age < 2:
    y = 'baby'
elif age >= 2 and age < 4:
    y = 'kid'
elif age >= 4 and age < 13:
    y = 'child'
elif age >= 13 and age < 20:
    y = 'teenager'
elif age >= 20 and age < 65:
    y = 'grown-up'
else:
    y = 'senior'

print(f"you are {y}")