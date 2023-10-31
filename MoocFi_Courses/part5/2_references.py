def double_items(numbers: list):
    result = []
    for i in numbers:
        result.append(i*2)
    return result

def remove_smallest(numbers: list):
    smallest = sorted(numbers)
    numbers = numbers.remove(smallest[0])


def print_sudoku(suduko: list):
    for row_no in range(len(suduko)):
        end_with = ''
        for col_no in range(len(suduko[row_no])):
            if col_no in [2, 5]:
                end_with = ' '
            else:
                end_with = ''
            if suduko[row_no][col_no] == 0:
                print('_ ', end=end_with)
            else:
                print(f'{suduko[row_no][col_no]} ', end=end_with)
        print()
        if row_no in [2, 5]:
            print()
def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku[row_no][column_no] += number

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku_copy = sudoku[:]
    sudoku_copy[row_no][column_no] = number
    return sudoku_copy

def play_turn(game_board: list, x: int, y: int, piece: str):
    if  0<=y<len(game_board) and 0<=x<len(game_board[0]) and game_board[y][x] == '':
        game_board[y][x] = piece
        return True
    else:
        return False


