x = [int(line.strip()) for line in open('input.txt')]
counter = 0

for i in range(1, len(x)):
    if x[i] > x[i-1]:
        counter += 1

print(counter, "measurements are larger than the previous.")
