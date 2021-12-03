from input import commands

horizontal = 0
depth = 0
aim = 0

for direction, ammount in commands:
    if direction == "forward":
        depth = depth + (ammount*aim)
        horizontal = horizontal + ammount
    else:
        if (direction == "down"):
            aim = aim + ammount
        else:
            aim = aim - ammount

print(horizontal*depth)