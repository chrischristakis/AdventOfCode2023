import math


def task1(path):
    with open(path, 'r') as file:
        directions = file.readline().rstrip()
        file.readline()

        path_pairs = {}
        # Iterate each path and the paths it points to, place them into a dict
        for line in file.readlines():
            line = line.rstrip()
            key, pair = line.split(' = ')
            left_path = pair[1:4]
            right_path = pair[6:9]
            path_pairs[key] = (left_path, right_path)

        # now, we follow directions until we reach 'ZZZ'
        next = 'AAA'
        counter = 0
        while next != 'ZZZ':
            dir = directions[counter % len(directions)]
            counter += 1
            if dir == 'L':
                next = path_pairs[next][0]
            else:
                next = path_pairs[next][1]
        return counter


def task2(path):
    with open(path, 'r') as file:
        directions = file.readline().rstrip()
        file.readline()

        path_pairs = {}
        current_paths = []
        # Iterate each path and the paths it points to, place them into a dict
        for line in file.readlines():
            line = line.rstrip()
            key, pair = line.split(' = ')
            left_path = pair[1:4]
            right_path = pair[6:9]
            path_pairs[key] = (left_path, right_path)

            if key[-1] == 'A':
                current_paths.append([key, 0])

        counter = 0
        cycles = []
        while len(cycles) != len(current_paths):
            dir = directions[counter % len(directions)]

            for i in range(0, len(current_paths)):
                curr, steps = current_paths[i]
                if curr[-1] == 'Z':
                    continue

                next = path_pairs[curr][0] if dir == 'L' else path_pairs[curr][1]
                if next[-1] == 'Z':
                    cycles.append(steps+1)

                current_paths[i] = [next, steps+1]
            counter += 1
        return math.lcm(*cycles)


print(task1('Day8.txt'))
print(task2('Day8.txt'))
