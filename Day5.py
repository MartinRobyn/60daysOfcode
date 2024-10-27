#Day 5
# Initialize an empty list to store names
names = []
# Loop to get 3 names from the user
for i in range(3):
    while True:
        try:
            name = input(f"Enter name{i+1}: ").strip()
            if not name:
                raise ValueError("Name cannot be empty.")
            names.append(name)
            break
        except ValueError as e:
            print(e)

for i, name in enumerate(names, start = 1):
    print(f"Name {i}: {name}")









       


