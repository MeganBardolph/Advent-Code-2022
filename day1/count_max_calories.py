#import pandas

max_calories  = 0
current_count = 0

with open('input_d01') as f:
    for line in f:
        if line == '\n':
            max_calories = max(max_calories, current_count)
            current_count = 0
        else:
            current_count = current_count + int(line)

print(max_calories)