with open('input.txt', 'r') as f:
    nums, *boards = f.read().split('\n\n')
    f.close()

nums = list(map(int, nums.split(',')))
bingo_boards = [[[int(i) for i in x.split()] for x in r.split('\n') if x] for r in boards]
called_nums = []
winner_board = []

for num in nums:
    if len(bingo_boards) == 0:
        break
    called_nums.append(num)
# check rows
    for board in bingo_boards:
        for line in board:
            if all(x in called_nums for x in line):
                winner_board = board
                bingo_boards.remove(winner_board)
                break

# check columns
    for j in range(0, 5):
        for boards in bingo_boards:
            column = []
            for lines in boards:
                column.append(lines[j])
            if all(x in called_nums for x in column):
                winner_board = boards
                bingo_boards.remove(winner_board)
                break

#sum of unmarked numbers
sum_win = 0
for line in winner_board:
    for i in line:
        if i not in called_nums:
            sum_win += i

score = sum_win * called_nums[-1]

print("Score of last possible board to win is:", score)
