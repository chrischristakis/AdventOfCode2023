import math

"""
We're gonna start with the naive approach, and just brute force the
distance for each time frame and store the maximum distance as we go along.
To calculate the distance each time in our range will travel, we use
distance = time_held * (time - time_held)
"""


def task1(path):
    with open(path, 'r') as file:

        time_str = file.readline().rstrip()[len('Time:'):]
        distance_str = file.readline().rstrip()[len('Distance:'):]

        times = [int(time) for time in time_str.split()]
        distances = [int(dist) for dist in distance_str.split()]
        list_len = len(times)  # note, these arrays are of equal length

        solution = 0
        for i in range(0, list_len):
            highscore = distances[i]
            ways_to_beat_highscore = 0
            for time_held in range(0, times[i]+1):
                dist = time_held * (times[i] - time_held)
                if dist > highscore:
                    ways_to_beat_highscore += 1
            solution = solution * ways_to_beat_highscore if solution > 0 else ways_to_beat_highscore
        return solution


"""
The naive approach will not work for such a big input, so we'll need to use some tricks.

when we iterate each time, our time_held is the dependant variable, and we want to find the 
time_held that gives us distances that exceed the high score.

If we expand our equation, we get this:
distance = (time_held * time) - time_held^2
which is a quadratic, with time_held being our dependant variable.

We want to find every time_held value where distance(time_held) > max_distance,
and return the length of that interval.

so if we plug in distance, we get
(time_held * time) - time_held^2 > max_distance

and isolate on the left isde so we get 0,
(time_held * time) - time_held^2 - max_distance > 0

This becomes an inequality we must find the roots for,
(time_held * time) - time_held^2 - max_distance = 0
               b         a             c
So plug these values into the quadratic formula, where 
a = -1
b = time
c = -max_distance

We can floor each root in the case it is a float.

And that becomes our interval, calculate the distance between the two values to get our answer.
"""


# O(1)
def task2(path):
    with open(path, 'r') as file:
        time_str = file.readline().rstrip()[len('Time:'):]
        distance_str = file.readline().rstrip()[len('Distance:'):]

        time = int(''.join(time_str.split()))
        highscore = int(''.join(distance_str.split()))

        quadratic_positive = (-time + math.sqrt(time*time - 4 * highscore)) // -2
        quadratic_negative = (-time - math.sqrt(time*time - 4 * highscore)) // -2
        return int(quadratic_negative - quadratic_positive)


print('Answer 1:', task1('Day6.txt'))
print('Answer 2:', task2('Day6.txt'))
