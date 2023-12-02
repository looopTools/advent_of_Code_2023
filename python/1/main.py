import argparse

tokens_mapping = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

def get_number(line_section) -> int:

    end = len(line_section)
    numbers = list()
    while end >= 2:
        if line_section[0: end] in tokens_mapping:
            return int(tokens_mapping[line_section[0: end]])
        end = end - 1
    return -1 

def task_one(lines) -> int:
    result = 0
    for line in lines:
        first = -1
        last = -1
        for i in range(0, len(line)):
            if ord(line[i]) >= 48 and ord(line[i]) <= 57:
                val = int(line[i])
                if first == -1:
                    first = val
                last = val
        result = result + (10 * first) + last
        
    
    return result

def task_two(lines) -> int:

    result = 0
    for line in lines:
        numbers = list()

        for i in range(0, len(line)):
            if ord(line[i]) >= 48 and ord(line[i]) <= 57:
                numbers.append(int(line[i]))
            else:

                found = False
                if i + 3 <= len(line):
                    val = get_number(line[i:i+3])
                    if val != -1:
                        numbers.append(val)
                        found = True
                if not found and i + 4 <= len(line):
                    val = get_number(line[i:i+4])
                    if val != -1:
                        numbers.append(val)
                        found = True
                if not found and i + 5 <= len(line):
                    val = get_number(line[i:i+5])
                    if val != -1:
                        numbers.append(val)

                                
                    
                # if i + 5 < len(line) - 1:
                #     if line[i:i+5] in tokens_mapping:
                #         numbers.append(tokens_mapping[line[i:i+5]])                
                # if i + 4 < len(line) - 1:
                #     if line[i:i+4] in tokens_mapping:
                #         numbers.append(tokens_mapping[line[i:i+4]])
                # if i + 3 < len(line) -1:
                #     if line[i:i+3] in tokens_mapping:
                #         numbers.append(tokens_mapping[line[i:i+3]])
                # if i < len(line) - 4:
                #     if line[i:] in tokens_mapping:
                #         print(tokens_mapping[line[i:]])
                #         numbers.append(tokens_mapping[line[i:]])
                

        if len(numbers) > 0:
            print(numbers)
            print((numbers[0] * 10) + numbers[-1])
            result = result + (numbers[0] * 10) + numbers[-1]
    return result

if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog='ac23 1', description='ac23 1')
    parser.add_argument('-d', '--data')
    parser.add_argument('-s', '--second', action='store_true')
    args = parser.parse_args()
    
    func = task_one

    if args.second:
        func = task_two


    lines = list()

    with open(args.data, 'r') as data_file:
        lines = data_file.readlines()
        lines = [line.replace('\n', '') for line in lines]

    result = func(lines)
    print(f'Result: {result}')
