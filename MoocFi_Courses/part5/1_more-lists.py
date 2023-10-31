def longest(strings: list):
    longest_ele = ''
    for i in strings:
        if len(i)>len(longest_ele):
            longest_ele = i
    return longest_ele

def count_matching_elements(my_matrix: list, element: int):
    sum = 0
    for row in my_matrix:
        sum += row.count(element)
    return sum

def who_won(game_board: list):
    player_1_score = 0
    player_2_score = 0
    for row in game_board:
        for box in row:
            if box == 1:
                player_1_score += 1
            elif box == 2:
                player_2_score += 1
    if player_1_score > player_2_score:
        return 1
    elif player_1_score < player_2_score:
        return 2
    else:
        return 0

def row_correct(sudoku: list, row_no: int):
    for n in range(1,10):
        if sudoku[row_no].count(n) > 1:
            return False
    return True

def column_correct(sudoku: list, column_no: int):
    col_val = []
    for i in range(len(sudoku)):
        col_val.append(sudoku[i][column_no])
    for i in range(1,10):
        if col_val.count(i) > 1:
            return False
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    flat_subsuduko = []
    for r in range(row_no, row_no+3):
        for c in range(column_no, column_no+3):
            flat_subsuduko.append(sudoku[r][c])
    for i in range(1, 10):
        if flat_subsuduko.count(i)>1:
            return False
    return True


def sudoku_grid_correct(sudoku: list):
    val = True
    for row_no in range(len(sudoku)):
        val = row_correct(sudoku, row_no)
        if val == False:
            return val

    for col_no in range(len(sudoku[0])):
        val = column_correct(sudoku, col_no)
        if val == False:
            return val

    for row_no in range(0, 7, 3):
        for col_no in range(0, 7, 3):
            val = block_correct(sudoku, row_no, col_no)
            if val == False:
                return val

    return val

