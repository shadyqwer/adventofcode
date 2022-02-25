with open('input.txt', 'r') as f:
    lines = f.read().split('\n')
    f.close()

# create lists with only coordinates
c = []
for line in lines:
    coords = ''.join((ch if ch in '0123456789' else ' ') for ch in line)
    coordinates = [int(i) for i in coords.split()]
    c.append(coordinates)

# finding max number
m = 0
for i in c:
    for j in i:
        if m <= j:
            m = j
# create empty list for calculation
output = []
for i in range(m+1):
    s = []
    for j in range(m+1):
        s.append(0)
    output.append(s)

# main loop
for i in range(0, len(c)):
    x1, y1, x2, y2 = c[i]

    if y1 == y2:
        if x1 >= x2:
            for n in range(x2, x1 + 1):
                output[n][y1] += 1
        else:
            for m in range(x1, x2 + 1):
                output[m][y1] += 1
    elif x1 == x2:
        if y1 >= y2:
            for j in range(y2, y1 + 1):
                output[x1][j] += 1
        else:
            for k in range(y1, y2 + 1):
                output[x1][k] += 1

    elif x1 > x2 and y1 > y2:
        if abs(x1 - x2) > abs(y1 - y2):
            output[x1][y1] += 1
            output[x2][y2] += 1
            for u in range(1, abs(x1 - x2)):
                output[x1 - u][y1 - u] += 1
        else:
            output[x1][y1] += 1
            output[x2][y2] += 1
            for u in range(1, abs(y1 - y2)):
                output[x1 - u][y1 - u] += 1

    elif x1 < x2 and y1 < y2:
        if abs(x1 - x2) > abs(y1 - y2):
            output[x1][y1] += 1
            output[x2][y2] += 1
            for u in range(1, abs(x1 - x2)):
                output[x1 + u][y1 + u] += 1
        else:
            output[x1][y1] += 1
            output[x2][y2] += 1
            for u in range(1, abs(y1 - y2)):
                output[x1 + u][y1 + u] += 1

    elif x1 > x2 and y1 < y2:
        if abs(x1 - x2) > abs(y1 - y2):
            output[x1][y1] += 1
            output[x2][y2] += 1
            for u in range(1, abs(x1 - x2)):
                output[x1 - u][y1 + u] += 1
        else:
            output[x1][y1] += 1
            output[x2][y2] += 1
            for u in range(1, abs(y1 - y2)):
                output[x1 - u][y1 + u] += 1

    elif x1 < x2 and y1 > y2:
        if abs(x1 - x2) > abs(y1 - y2):
            output[x1][y1] += 1
            output[x2][y2] += 1
            for u in range(1, abs(x1 - x2)):
                output[x1 + u][y1 - u] += 1
        else:
            output[x1][y1] += 1
            output[x2][y2] += 1
            for u in range(1, abs(y1 - y2)):
                output[x1 + u][y1 - u] += 1

# get how much are larger than 2
counter = 0
for i in output:
    for j in i:
        if j >= 2:
            counter += 1

print(counter)