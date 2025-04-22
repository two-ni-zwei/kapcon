#!/usr/bin/env python3

# Performs Kaprekars routine on a given 4 digit integer or all digits in range 1000 - 9999
# Invoke the script with <A 4 digit integer> or --all

import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

KAPREKARS_CONSTANT = 6174

def next_in_sequence(digits : str, iteration : int, log_output=True) -> int:
    arranged_highest = descending(digits)
    arranged_lowest = ascending(digits)
    while (len(str(arranged_highest))) < 4:
        arranged_highest = int(str(arranged_highest) + str('0'))
    
    l_output = str(arranged_lowest)
    while (len(l_output)) < 4:
        l_output = str('0') + l_output
    next = arranged_highest - arranged_lowest
    output = f'{arranged_highest} - {l_output} = {next}'
    
    if log_output:
        print(f'Iteration: {iteration} | Next {digits}\n{output}')
    return next

def descending(digits : str) -> int:
    sort_descend = sorted(list(digits), reverse=True)
    return int(''.join(sort_descend))

def ascending(digits : str) -> int:
    sort_ascend = sorted(list(digits))
    return int(''.join(sort_ascend))

def repeating_digits(digits : str) -> bool:
    return all(i == digits[0] for i in digits)

def kaprekars_routine(digits : str, log_output = True) -> [int]:
    iteration = 1
    sequence = [int(digits)]

    while True:
        next = next_in_sequence(digits, iteration, log_output)
        sequence.append(next)
        if next == KAPREKARS_CONSTANT:
            break
        else:
            digits = str(next)
        iteration += 1
    if log_output:
        print(f'Finished after {iteration} iterations.')
    return sequence

def kaprekars_range() -> None:
    for i in range(1000, 9999):
        if repeating_digits(str(i)):
            continue
        sequence = kaprekars_routine(str(i), log_output=False)
        if len(sequence) >= 7:
            print(f'{bcolors.OKCYAN}{sequence}{bcolors.ENDC}')
        else:
            print(sequence)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('No input given.')
        quit()

    if '--all' in sys.argv:
        kaprekars_range()
    else:
        digits = sys.argv[1]

        if len(digits) != 4:
            print('Input must be a 4 digit value.')
            quit()

        if repeating_digits(digits):
            print('Input must not contain 4 repeating digits.')
            quit()

        kaprekars_routine(digits)
