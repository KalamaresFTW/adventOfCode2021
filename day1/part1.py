from input import vals

i = 0
lenght = len(vals)-1

for idx, val in enumerate(vals):
    if (idx<lenght):
        if (vals[idx+1] > vals[idx]):
            i = i + 1

print(i)