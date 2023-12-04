def task1(path):
    with open(path, 'r') as file:
        lines = [line.rstrip() for line in file.readlines()]
        max_red = 12
        max_blue = 14
        max_green = 13
        valid_rounds = 0
        for line in lines:
            game_info, rounds = line.split(": ")
            game_id = game_info.split(' ')[-1]

            rounds = rounds.split('; ')

            valid = True
            for round in rounds:
                pulls = round.split(', ')
                for pull in pulls:
                    num, color = pull.split(' ')
                    num = int(num)
                    if color == 'green' and num > max_green or \
                       color == 'blue' and num > max_blue or \
                       color == 'red' and num > max_red:
                        valid = False
                        break
                if not valid:
                    break
            if valid:
                valid_rounds += int(game_id)
        return valid_rounds


def task2(path):
    with open(path, 'r') as file:
        lines = [line.rstrip() for line in file.readlines()]

        sum = 0
        for line in lines:
            game_info, rounds = line.split(": ")
            game_id = game_info.split(' ')[-1]
            rounds = rounds.split('; ')

            maxpulls = {'red': 0, 'blue': 0, 'green': 0}
            for round in rounds:
                pulls = round.split(', ')
                for pull in pulls:
                    num, color = pull.split(' ')
                    num = int(num)

                    maxpulls[color] = max(maxpulls[color], num)

            power = maxpulls['red'] * maxpulls['green'] * maxpulls['blue']
            sum += power
        return sum


print(task1("Day2.txt"))
print(task2("Day2.txt"))
