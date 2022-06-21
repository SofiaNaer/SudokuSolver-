
def solve(bo):
    find = find_empty(bo)
    if None == find:
        return True
    row = find[0]
    column = find[1]
    for i in range(1, 10):
        if findValid(bo, i, (row, column)):
            bo[row][column] = i

            if solve(bo):
                return True

            bo[row][column] = 0
    return False


def findValid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def printBoard(bo):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")

        for j in range(len(bo[i])):

            if j % 3 == 0 and j != 0:
                print("|", end="")
            if j == 8:
                print(str(bo[i][j]) + " ")

            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[i])):
            if bo[i][j] == 0:
                return i, j
    return None



