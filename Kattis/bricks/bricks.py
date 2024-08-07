from sys import stdin


def rotate_right(formation):
    cols = len(formation[0])
    rows = len(formation)
    return [[formation[i][j] for i in range(rows)] for j in range(cols)]


def flatten(formation):
    vals = [0] * len(formation[0])
    for row in formation:
        for j in range(len(row)):
            if row[j]:
                vals[j] += 1
    return vals


def add_formation(board, flat_formation, offset):
    new_board = [x for x in board]
    collapses = 0
    for i in range(len(flat_formation)):
        j = i + offset
        new_board[j] += flat_formation[i]
        if new_board[j] >= 3:
            collapses += new_board[j]
            new_board[j] = 0
    return tuple(new_board), collapses


def f(round, board, mem):
    if round >= len(round_list):
        return 0
    if (round, board) in mem:
        return mem[(round, board)]

    formation, s = round_list[round]
    flat_up = flatten(formation)
    flat_right = flatten(rotate_right(formation))
    flat_down = [x for x in reversed(flat_up)]
    flat_left = [x for x in reversed(flat_right)]

    best_score = -1
    for flat_form in (flat_up, flat_left, flat_down, flat_right):
        for offset in range(len(board) - len(flat_form) + 1):
            new_board, collapses = add_formation(board, flat_form, offset)
            score = s * collapses + f(round + 1, new_board, mem)
            best_score = max(best_score, score)

    mem[(round, board)] = best_score
    return best_score


n = int(stdin.readline())
round_list = []
for _ in range(n):
    w, h, s = map(int, stdin.readline().split())
    formation = [
        [True if x == "#" else False for x in stdin.readline().rstrip()]
        for _ in range(h)
    ]
    round_list.append((formation, s))

board = tuple(0 for _ in range(6))
print(f(0, board, {}))
