from collections import defaultdict, Counter


def valid_in_range(line: str) -> bool:
    """Check passwords file lines against the associated rule
    This means counting the number of times a letter appears
    and checking that it is within the desired range"""
    letters = defaultdict(int)
    fields = line.split(' ')
    if len(fields) == 3:
        for ch in fields[2]:
            letters[ch] += 1

        nums = fields[0].split('-')
        how_many = letters[fields[1][0]]
        if int(nums[0]) <= how_many <= int(nums[1]):
            return True
    else:
        print(f'ERROR - bad input line ->{line}')
    return False


def valid_by_position(line: str) -> bool:
    """Check password line checking that desired char appears in EXACTLY one of the positions"""
    fields = line.split(' ')
    if len(fields) == 3:
        match_count = 0
        nums = fields[0].split('-')
        if fields[2][int(nums[0])-1] == fields[1][0]:
            match_count += 1
        if fields[2][int(nums[1])-1] == fields[1][0]:
            match_count += 1
        if match_count == 1:
            return True
    else:
        print(f'ERROR - bad input line ->{line}')
    return False


def check_passwords(infile: str, val_chk) -> int:

    valid_count = 0

    with open(infile) as inf:
        for line in inf.read().splitlines():
            if val_chk(line):
                valid_count += 1

    return valid_count


print('Part 1')
checker = valid_in_range
assert check_passwords('../data/test02.txt', checker) == 2

pass_count = check_passwords('../data/input02.txt', checker)
print(pass_count)

print('\nPart 2')
checker = valid_by_position
assert check_passwords('../data/test02.txt', checker) == 1

pass_count = check_passwords('../data/input02.txt', checker)
print(pass_count)
