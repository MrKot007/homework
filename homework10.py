sequence = []
dominant_pairs = 0
while True:
    character = int(input('sequence '))
    sequence.append(character)
    if character == 0:
        sequence.append(0)
        break
for i in range(len(sequence)):
    if sequence[i] < sequence[i+1]:
        dominant_pairs+=1
    else:
        continue
print(dominant_pairs)