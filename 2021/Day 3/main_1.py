x = [(line.strip()) for line in open('input.txt')]
count0 = 0
count1 = 0
gamma = 0
epsilon = 0

for j in range(len(x[0])):
    for i in range(len(x)):
        if x[i][j] == '1':
            count1 += 1
        elif x[i][j] == '0':
            count0 += 1
    if count1 > count0:
        gamma += (10 ** (len(x[0])-j-1))
    else:
        epsilon += (10 ** (len(x[0])-j-1))
    count0 = 0
    count1 = 0

gamma = int(str(gamma), 2)
epsilon = int(str(epsilon), 2)

power = gamma * epsilon
print(power)
