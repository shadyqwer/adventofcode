x = [int(line.strip()) for line in open('input.txt')]

counter = 0
for i in range(len(x)):
    if i == len(x) - 3:
        break
    tm1 = x[i] + x[i + 1] + x[i + 2]
    tm2 = x[i + 1] + x[i + 2] + x[i + 3]
    if tm2 > tm1:
        counter += 1
        
print(counter)
