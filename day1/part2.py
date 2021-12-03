from input import vals

incrementado = 0
lenght = len(vals)-3

for idx, val in enumerate(vals):
    if (idx<lenght):
        if ((vals[idx+1] + vals[idx+2] + vals[idx+3]) > (vals[idx] + vals[idx+1] + vals[idx+2])):
            incrementado = incrementado + 1

print(incrementado)