import re


def find_first_number(line):
    for char in line:
        if char.isdigit():
            return char


def find_last_number(line):
    for char in reversed(line):
        if char.isdigit():
            return char


def day_1_part_1():
    sum = 0
    with open("./inputs/Day1Input.txt", "r") as file:
        for line in file:
            first_digit = find_first_number(line)
            last_digit = find_last_number(line)
            first_number = first_digit + last_digit
            sum += int(first_number)
    return sum


wordToInt = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def convert_to_int(s):
    if wordToInt.get(s) is not None:
        return wordToInt[s]
    else:
        return int(s)


def day_1_part_2():
    sum = 0
    with open("./inputs/Day1Input.txt", "r") as file:
        for line in file:
            matches = re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)
            fnum = convert_to_int(matches[0])
            lnum = convert_to_int(matches[len(matches) - 1])
            sum += fnum * 10 + lnum

    return sum


if __name__ == '__main__':
    day_1_solution = day_1_part_1()
    print(f"Day 1 Solution: {day_1_solution}")

    day_2_solution = day_1_part_2()
    print(f"Day 1 Part 2 Solution: {day_2_solution}")
