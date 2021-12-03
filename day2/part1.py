from input import commands

i = 0

horizontal = 0
depth = 0

for direction, ammount in commands:
    if direction == "forward":
        horizontal = horizontal + ammount
    else:
        if (direction == "down"):
            depth = depth + ammount
        else:
            depth = depth - ammount

print(horizontal*depth)