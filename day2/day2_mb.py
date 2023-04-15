round_scores = {
    "A X": 3,
    "A Y": 6,
    "A Z": 0,
    "B X": 0,
    "B Y": 3,
    "B Z": 6,
    "C X": 6,
    "C Y": 0,
    "C Z": 3
}

shape_values = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

total_score = 0
round_points = []

with open("input_d02") as f:
    for round in f:
        round_score = round_scores[round.strip()]
        shape_value = shape_values[round[2]]
        points = round_score + shape_value
        round_points.append(points)
        total_score = total_score + points

print("Part 1 total:\t",total_score)

# Part 2

round_scores_2 = {
    "A X": 3, # Lose (Scissors)
    "A Y": 4, # Draw (Rock)
    "A Z": 8, # Win  (Paper)
    "B X": 1, # Lose (Rock)
    "B Y": 5, # Draw (Paper)
    "B Z": 9, # Win  (Scissors)
    "C X": 2, # Lose (Paper)
    "C Y": 6, # Draw (Scissors)
    "C Z": 7  # Win  (Rock)
}

total_score = 0
round_points = []

with open("input_d02") as f:
    for round in f:
        round_score = round_scores_2[round.strip()]

        round_points.append(round_score)
        total_score = total_score + round_score

print("Part 2 total:\t",total_score)