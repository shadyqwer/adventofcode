x = [(line.strip()) for line in open('input.txt')]
y = [(line.strip()) for line in open('input.txt')]

count0 = 0
count1 = 0


def removex(list, num, position):
    for i in range(len(list)-1, -1, -1):
        if len(list) == 1:
            break
        if list[i][position] == num:
            list.remove(list[i])


while len(x) != 1:
    for j in range(len(x[0])):
        for i in range(len(x)):
            if x[i][j] == '1':
                count1 += 1
            elif x[i][j] == '0':
                count0 += 1
        if count1 >= count0:
            removex(x, '0', j)
        else:
            removex(x, '1', j)
        count0 = 0
        count1 = 0

while len(y) != 1:
    for j in range(len(y[0])):
        for i in range(len(y)):
            if y[i][j] == '1':
                count1 += 1
            elif y[i][j] == '0':
                count0 += 1
        if count0 <= count1:
            removex(y, '1', j)
        else:
            removex(y, '0', j)

        count0 = 0
        count1 = 0

oxygen = int(str(x[0]), 2)
co = int(str(y[0]), 2)

lsr = oxygen * co
print(lsr)
