"""
The general process is to check if the seed number is source <= seed_num < source + range
Then, calculate the destination seed num by doing destination + (seed_num - source) which will give
you the translated seed num.
"""


def task1(path):
    with open(path, 'r') as file:
        line = file.readline().rstrip()  # first line is seeds
        line = line.split(': ')[1]
        seeds = [int(seed) for seed in line.split(' ')]

        ranges = []

        def transform_seeds(seeds, ranges):
            for i in range(0, len(seeds)):
                for dest, source, span in ranges:
                    if source <= seeds[i] < (source + span):
                        diff = seeds[i] - source
                        seeds[i] = dest + diff
                        break  # found a match, no need to continue

        skip_next = False
        for line in file.readlines():
            if skip_next:
                skip_next = False
                continue

            line = line.rstrip()

            # On blank lines, we check the seeds against the current ranges and translate them, then
            # empty ranges to be filled with new ones.
            if not line:
                transform_seeds(seeds, ranges)
                ranges = []
                skip_next = True
            else:
                ranges.append([int(num) for num in line.split(' ')])

        transform_seeds(seeds, ranges) # remaining seeds since file terminates a line early.
        return min(seeds)

"""
task 2 is pretty similar, just transform seed pairs initially into a range.
... but the original solution now takes way too long, so we need to be smart about it.

So instead, we're gonna keep the (seeds, span) pairings like the questions states, without splitting into a
range. The only time we split a seed into a new seed pair is when it is only a portion of it is translated, then
turn that portion into one seed and the remainder into another.
"""

def task2(path):
    with open(path, 'r') as file:
        line = file.readline().rstrip()  # first line is seeds
        line = line.split(': ')[1]
        seeds = [int(seed) for seed in line.split(' ')]
        seed_pairs = []
        for i in range(0, len(seeds), 2):
            seed_pairs.append([seeds[i], seeds[i] + seeds[i+1] - 1])

        ranges = []

        def transform_seeds(seed_pairs, ranges):
            for i in range(0, len(seed_pairs)):
                seed_begin, seed_end = seed_pairs[i]
                for dest, source, span in ranges:
                    src_range = [source, source + span - 1]

                    # Find if the seed and src ranges overlap and by how much
                    overlap_start = max(seed_begin, src_range[0])
                    overlap_end = min(seed_end, src_range[1])
                    overlap_count = overlap_end - overlap_start + 1

                    if overlap_count > 0:
                        # if there's overlap, we break the overlap down to only the part that
                        # fits into the overlap, the rest gets turned into a new seed bar
                        trimmed_begin = seed_begin
                        trimmed_end = seed_end

                        #case 1: seed overhangs to the left of the overlap, trim off left bit
                        if seed_begin < overlap_start:
                            num_left_trimmed = source - seed_begin

                            # Add left trimmed portion back into array
                            seed_pairs.append([seed_begin, seed_begin + num_left_trimmed - 1])

                            trimmed_begin = overlap_start
                        #case 2: right overhang
                        if seed_end > overlap_end:
                            seed_pairs.append([overlap_end + 1, seed_end])

                            trimmed_end = overlap_end

                        offset_begin = max(0, trimmed_begin - source)
                        offset_end = max(0, trimmed_end - source)

                        # translate the part that fits into the overhang into a new range
                        trimmed = [dest + offset_begin, dest + offset_end]

                        seed_pairs[i] = trimmed
                        break  # found a range, no need to continue iterating.

        skip_next = False
        for line in file.readlines():
            line = line.rstrip()
            if skip_next:
                skip_next = False
                continue

            # On blank lines, we check the seeds against the current ranges and translate them, then
            # empty ranges to be filled with new ones.
            if not line:
                transform_seeds(seed_pairs, ranges)
                ranges = []
                skip_next = True
            else:
                ranges.append([int(num) for num in line.split(' ')])

        transform_seeds(seed_pairs, ranges)  # remaining seeds since file terminates a line early.

        min_seed = float('+inf')
        for seed_src, span in seed_pairs:
            min_seed = min(min_seed, seed_src)

        # Return the smallest starting number in our set ouf number ranges
        return min_seed


print(task1('Day5.txt'))
print('Answer: ', task2('Day5.txt'))
#10834440
