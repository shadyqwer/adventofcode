x = [line.strip() for line in open('input.txt')]

horizontal = 0
depth = 0
aim = 0

for i in range(len(x)):
    if 'forward' in x[i]:
        horizontal += (int(x[i][-1:]))
        depth += (aim * (int(x[i][-1:])))
    elif 'up' in x[i]:
        aim -= (int(x[i][-1:]))
    elif 'down' in x[i]:
        aim += (int(x[i][-1:]))

print(horizontal * depth)