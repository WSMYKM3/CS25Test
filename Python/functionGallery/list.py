scores = []

for _ in range(3):
    score = int(input("Score: "))
    scores.append(score)
    ##scores += [score]

avg = sum(scores) / len(scores)

print(f"Average: {avg}")        