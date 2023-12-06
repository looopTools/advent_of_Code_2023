import argparse

SYMBOLS = ['*', '#', '$', '+']
NON_SYMBOL = '.'

def is_part_number(row: int, start_col: int, end_col: int, puzzle: list[list[str]]) -> bool:

    if start_col != 0 and puzzle[row][start_col - 1] != NON_SYMBOL:
            return True
    if end_col != len(puzzle[row]) - 1 and puzzle[row][end_col + 1] != NON_SYMBOL:
            return True
        
    other_start = start_col
    
    if other_start != 0:
        other_start = other_start - 1

    other_end = end_col
    
    if other_end != len(puzzle[row]) - 1:
        other_end = other_end + 1

    if row != 0:
        for i in range(other_start, other_end + 1):
            if puzzle[row - 1][i] != NON_SYMBOL:
                return True

    if row != len(puzzle) - 1:
        for i in range(other_start, other_end + 1):

            if puzzle[row + 1][i] != NON_SYMBOL:
                return True
    return False


def convert_to_number(row: int, start_col: int, end_col: int, puzzle: list[list[str]]) -> int:

    num = 0
    mul = 10
    for i in range(start_col, end_col + 1):
        num = (num * mul) + int(puzzle[row][i])
        mul = mul 
        
    return num

def find_part_numbers(puzzle: list[list[str]]) -> list[int]:

    part_numbers = list()
    for row in range(0, len(puzzle)):

        start_number = -1
        end_number = -1

        for col in range(0, len(puzzle[row])):
            if ord(puzzle[row][col]) >= 48 and ord(puzzle[row][col]) <= 57:
                if start_number == -1:
                    start_number = col
                    end_number = col
                else:
                    end_number = col
            else:
                if start_number != -1:
                    if is_part_number(row, start_number, end_number, puzzle):
                        num = convert_to_number(row, start_number, end_number, puzzle)
                        part_numbers.append(num)
                    start_number = -1
                    end_number = -1

        if start_number != -1:
            if is_part_number(row, start_number, end_number, puzzle):
                num = convert_to_number(row, start_number, end_number, puzzle)
                part_numbers.append(num)
    return part_numbers
                    
def sum_part_numbers(puzzle: list[list[str]]) -> int:

    result = 0
    for num in find_part_numbers(puzzle):
        result = result + num
    return result



def find_part_numbers_adjacent_to_gear(puzzle: list[list[str]]):

    



if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog='ac23 3', description='ac23 3')
    parser.add_argument('-d', '--data')
    parser.add_argument('-s', '--second', action='store_true')
    args = parser.parse_args()

    lines = None 
    with open(args.data, 'r') as data_file:
        lines = data_file.readlines()
        lines = [line.replace('\n', '') for line in lines]
        
    result = 0
    if not args.second:
        result = sum_part_numbers(lines)
    else:
        result = -1
        
    print(result)
