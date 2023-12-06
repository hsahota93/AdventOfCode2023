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


if __name__ == '__main__':
    day_1_solution = day_1_part_1()
    print(f"Day 1 Solution: {day_1_solution}")
