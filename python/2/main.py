import argparse

def convert_data(line):

    game_id = line[:line.index(':')]
    game_id = int(game_id.split(' ')[-1])


    game_draws = line[line.index(':') +1:].strip().split(';')

    draws = list()
    for game_draw in game_draws:
        game_draw = game_draw.split(',')
        color_map = {}
        for draw in game_draw:
            draw = draw.strip().split(' ')
            color_map[draw[1]] = int(draw[0])
        draws.append(color_map)
    return game_id, draws
        

def find_highest_number_of_color(color: str, game: list[dict[str,int]]) -> int:
    result = 0

    for draw in game:

        if color in draw and result < draw[color]:
            result = draw[color]
    return result

def find_highest_number_of_dice(game: list[dict[str,int]]) -> int:
    result = 0
    for draw in game:
        number_of_dice = 0
        for _, value in draw.items():
            number_of_dice = number_of_dice + value
        if result < number_of_dice:
            result = number_of_dice
    return result
    

def is_possible_game(red: int, green: int, blue: int, game: list[dict[str,int]]) -> bool:

    total_num_of_dice = red + green + blue

    if total_num_of_dice < find_highest_number_of_dice(game):
        return False

    if red < find_highest_number_of_color('red', game):
        return False


    if green < find_highest_number_of_color('green', game):
        return False
    
    if blue < find_highest_number_of_color('blue', game):
        return False

    return True
    

def number_of_valid_games(red: int, green: int, blue: int, games: [int, list[dict[str, int]]]) -> int:
    result = 0

    for game, draws in games.items():
        if is_possible_game(red, green, blue, draws):
            result = result + game
    return result

def get_minimal_viable_number_of_dice(game: list[dict[str, int]]) -> int:

    red = 0
    green = 0
    blue = 0

    for draw in game:
        for color, value in draw.items():
            if color == 'red' and red < value:
                red = value
            if color == 'green' and green < value:
                green = value
            if color == 'blue' and blue < value:
                blue = value                
    
    return red * green * blue

    
    
def get_number_of_power_sumation(games: [int, list[dict[str, int]]]) -> int:
    result = 0

    for _, game in games.items():
        result = result + get_minimal_viable_number_of_dice(game)
    
    return result
    
if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog='ac23 2', description='ac23 2')
    parser.add_argument('-d', '--data')
    parser.add_argument('-s', '--second', action='store_true')
    args = parser.parse_args()

    lines = None 
    with open(args.data, 'r') as data_file:
        lines = data_file.readlines()
        lines = [line.replace('\n', '') for line in lines]


    games = {}
    for line in lines:
        id, draws = convert_data(line)
        games[id] = draws

    result = 0
    if not args.second:
        result = number_of_valid_games(12, 13, 14, games)
    else:
        result = get_number_of_power_sumation(games)
        
    print(result)
    # func = task_one

    # if args.second:
    #     func = task_two


    # lines = list()

    # with open(args.data, 'r') as data_file:
    #     lines = data_file.readlines()
    #     lines = [line[:-1] for line in lines]

    # result = func(lines)
    # print(f'Result: {result}')
