

lines = ["0 1 2 4", "0 9", "0 5 2"]

for line in lines[1:]:
    if len(line.split()) != 2:
        continue  # Skip this iteration (invalid format of point)

    print(line)

