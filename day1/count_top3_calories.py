all_calories = []
current_count = 0

with open('input_d01') as f:
    for line in f:
        if line == '\n':
            all_calories.append(current_count)
            current_count = 0
        else:
            current_count = current_count + int(line)

print('Three highest values:\t', sorted(all_calories)[-3:])
print('Sum of top three values:\t',sum(sorted(all_calories)[-3:]))