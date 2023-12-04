def task1(path):
    with open(path, "r") as file:
        lines = [line.rstrip() for line in file.readlines()]
        digits = []
        for line in lines:
            digit = ""
            for c in line:
                if c.isnumeric():
                    digit += c
                    break
            for c in line[::-1]:
                if c.isnumeric():
                    digit += c
                    break
            digits.append(int(digit))
        return sum(digits)


"""
Since some characters from one number can contribute to characters in another number
(think 'fiveight' should be read as 58)
We can just replace 'one' with a 1.
Instead, we will replace 'one' with 'one1one' so that the characters to the left and right of it
are unaffected and can use the characters in the word 'one'
"""


def task2(path):
    with open(path, "r") as file:
        lines = [line.rstrip() for line in file.readlines()]

        digits = []
        for line in lines:
            modified = \
                line.replace('one', 'one1one') \
                .replace('two', 'two2two') \
                .replace('three', 'three3three') \
                .replace('four', 'four4four') \
                .replace('five', 'five5five') \
                .replace('six', 'six6six') \
                .replace('seven', 'seven7seven') \
                .replace('eight', 'eight8eight') \
                .replace('nine', 'nine9nine')

            digit = ""
            for c in modified:
                if c.isnumeric():
                    digit += c
                    break
            for c in modified[::-1]:
                if c.isnumeric():
                    digit += c
                    break
            digits.append(int(digit))
        return sum(digits)


print(task1("Day1.txt"))
print(task2("Day1.txt"))
