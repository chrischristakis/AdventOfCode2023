def task1(path, part2=False):
    with open(path, 'r') as file:
        ans = 0
        for line in file.readlines():
            line = line.rstrip()

            # Work up the stack until we have an array with all zeroes
            stack = [[int(num) for num in line.split(' ')]]
            all_zeroes = False
            while not all_zeroes:
                diffs = []
                current_list = stack[-1]
                for i in range(1,len(current_list)):
                    diffs.append(current_list[i] - current_list[i-1])
                stack.append(diffs)
                all_zeroes = all(num == 0 for num in diffs)

            # Now, the all zero array should be at the top of our stack.
            # All we must do is insert a new element which is the sum of the last element from this
            # list and previous list.
            last_element = 0
            while stack:
                current = stack.pop()
                if part2:
                    last_element = current[0] - last_element
                else:
                    last_element = current[-1] + last_element
            ans += last_element
        return ans


print(task1("Day9.txt"))
print(task1("Day9.txt", True))
