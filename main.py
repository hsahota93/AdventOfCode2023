def find_first_number(line):
    for char in line:
        if char.isdigit():
            return char


def find_last_number(line):
    for char in reversed(line):
        if char.isdigit():
            return char


if __name__ == '__main__':

    sum = 0
    with open("./inputs/Day1Input.txt", "r") as file:
        for line in file:
            first_digit = find_first_number(line)
            last_digit = find_last_number(line)
            first_number = first_digit + last_digit
            sum += int(first_number)
    print(sum)
