def task1(path):
    with open(path, 'r') as file:
        total = 0
        for line in file.readlines():
            line = line.rstrip().split(': ')[1]  # remove anything before the ': '

            winning_nums, my_nums = line.split(' | ')
            winning_nums = winning_nums.split()  # removes padded spaces
            my_nums = my_nums.split()

            # loop through and check if numbers appear in set.
            # this assumes no duplicates exist
            winning_nums = set(winning_nums)
            score = 0
            for num in my_nums:
                if num in winning_nums:
                    score = score*2 if score > 0 else 1
            total += score

        return total


"""
Part 2 is a little tricky, but if we have a map that correlates to the number of copies of each card, we
increment the following cards that we won from the current ones by the number of copies of our current card.
- Note, we start off with 1 copy of each card.
e.g. Card 1 has 3 matching numbers, so we get one copy of 2,3,4 
card copies
1    1
2    1
3    1
4    1
5    1
Now, if card 2 has 2 matching numbers, increment each by the amount of copies we have of card 2
1    1
2    1
3    1+1=2
4    1+1=2
5    1
Now, if card 3 has 2 matching, increment each by the amount of card 3 copies
1    1
2    1
3    2
4    2+2=4
5    1+2=3
Do this until the end.
"""


def task2(path):
    with open(path, 'r') as file:

        copy_map = {}  # Key: card num, value: num copies

        for line in file.readlines():
            info, line = line.rstrip().split(': ')
            card_num = int(info.split()[1])

            if card_num not in copy_map:
                copy_map[card_num] = 1

            winning_nums, my_nums = line.split(' | ')
            winning_nums = winning_nums.split()
            my_nums = my_nums.split()

            winning_nums = set(winning_nums)
            matches = 0
            for num in my_nums:
                if num in winning_nums:
                    matches += 1

            # Our number of matches is the number of next cards we win
            for i in range(1, matches+1):
                if card_num+i not in copy_map:
                    copy_map[card_num+i] = 1
                copy_map[card_num+i] += copy_map[card_num]

        return sum(copy_map.values())


print(task1('Day4.txt'))
print(task2('Day4.txt'))
