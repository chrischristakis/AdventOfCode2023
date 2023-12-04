def task1(path):
    with open(path, 'r') as file:
        lines = [line.rstrip() for line in file.readlines()]

        rows = len(lines)
        cols = len(lines[0])

        found_num_coords = set()

        def construct_num(x, y):
            l = x-1
            left = ""
            while l >= 0 and lines[y][l].isnumeric():
                if lines[y][l].isnumeric():
                    left = lines[y][l] + left
                    found_num_coords.add((l, y))
                l -= 1

            r = x + 1
            right = ""
            while r <= cols-1 and lines[y][r].isnumeric():
                if lines[y][r].isnumeric():
                    right = right + lines[y][r]
                    found_num_coords.add((r, y))
                r += 1
            found_num_coords.add((x, y))
            return left + lines[y][x] + right

        part_sum = 0
        for y in range(0, rows):
            for x in range(0, cols):
                if lines[y][x].isnumeric() or lines[y][x] == '.':
                    continue

                # check all adjacent cells to current one
                left_index = x-1 if (x > 0) else x
                right_index = x+1 if (x < cols-1) else x
                top_index = y-1 if (y > 0) else y
                bottom_index = y+1 if (y < rows-1) else y
                for adj_y in range(top_index, bottom_index+1):
                    for adj_x in range(left_index, right_index+1):
                        if lines[adj_y][adj_x].isnumeric() and (adj_x, adj_y) not in found_num_coords:
                            num_str = construct_num(adj_x, adj_y)
                            part_sum += int(num_str)
        return part_sum


def task2(path):
    with open(path, 'r') as file:
        lines = [line.rstrip() for line in file.readlines()]

        rows = len(lines)
        cols = len(lines[0])

        def construct_num(x, y):
            l = x-1
            left = ""
            while l >= 0 and lines[y][l].isnumeric():
                if lines[y][l].isnumeric():
                    left = lines[y][l] + left
                l -= 1

            r = x + 1
            right = ""
            while r <= cols-1 and lines[y][r].isnumeric():
                if lines[y][r].isnumeric():
                    right = right + lines[y][r]
                r += 1
            return left + lines[y][x] + right

        part_sum = 0
        for y in range(0, rows):
            for x in range(0, cols):
                if lines[y][x] != '*':
                    continue

                # check all adjacent cells to current one
                found_nums = set()
                left_index = x-1 if (x > 0) else x
                right_index = x+1 if (x < cols-1) else x
                top_index = y-1 if (y > 0) else y
                bottom_index = y+1 if (y < rows-1) else y
                for adj_y in range(top_index, bottom_index+1):
                    for adj_x in range(left_index, right_index+1):
                        if lines[adj_y][adj_x].isnumeric():
                            num_str = construct_num(adj_x, adj_y)
                            if num_str not in found_nums:
                                found_nums.add(num_str)

                if len(found_nums) == 2:
                    first_gear, second_gear = list(found_nums)
                    part_sum += int(first_gear) * int(second_gear)
        return part_sum


print(task1('Day3.txt'))
print(task2('Day3.txt'))
