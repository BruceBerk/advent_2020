import numpy as np


def toboggan_trees(infile: str, go_right: int, go_down: int) -> int:
    """move the toboggan down the supplied map and count the trees ('#')"""
    trees = 0
    toboggan_run = []

    # read the map into a list
    with open(infile) as inf:
        for line in inf.read().splitlines():
            toboggan_run.append(line)

    row_max = len(toboggan_run)
    col_max = len(toboggan_run[0])

    row = 0
    col = 0
    while row < (row_max - go_down):
        row += go_down
        col += go_right
        if col >= col_max:
            col -= col_max
        if toboggan_run[row][col] == '#':
            trees += 1

    return trees


print("part 1")
assert toboggan_trees('../data/test03.txt', 3, 1) == 7

tree_count = toboggan_trees('../data/input03.txt', 3, 1)
print(tree_count)

print("part 2")
tries = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
tree_counts = []

for move in tries:
    tree_counts.append(toboggan_trees('../data/test03.txt', move[0], move[1]))

print(np.prod(tree_counts))

tree_counts = []
for move in tries:
    tree_counts.append(toboggan_trees('../data/input03.txt', move[0], move[1]))

print(np.prod(tree_counts))
