import argparse


def clean_up_data(data: list[str]):

    entries = []
    for line in data:
        line = line[line.index(':') + 1:].split('|')

        entry = list()
        for part in line:
            part = part.split(' ')
            part = [int(p) for p in part if p != '']
            entry.append(part)
        entries.append(entry)
    return entries
            
def find_winning_numbers_weight(winner_numbers: list[int], draw: list[int]) -> int:
    result = 0

    for num in draw:
        if num in winner_numbers:
            if result == 0:
                result = 1
            else:
                result = result * 2
    
    return result

def finding_combined_weight(data) -> int:
    total = 0
    for entry in data:
        total = total + find_winning_numbers_weight(entry[0], entry[1])
    return total


def find_number_of_scratch_cards(data) -> int:

    return 0

if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog='ac23 3', description='ac23 3')
    parser.add_argument('-d', '--data')
    parser.add_argument('-s', '--second', action='store_true')
    args = parser.parse_args()

    lines = None 
    with open(args.data, 'r') as data_file:
        lines = data_file.readlines()
        lines = [line.replace('\n', '') for line in lines]
    lines = clean_up_data(lines)
    result = 0
    if not args.second:
        result = finding_combined_weight(lines)
    else:
        result = find_number_of_scratch_cards(data)
    
    print(result)
