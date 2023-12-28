from helper import *

data = raw_data(2023, 6)
lines = lines(data)


def solutions_of(total_time, goal_distance):
    for press_duration in range(total_time):
        run_distance = (total_time - press_duration) * press_duration
        if run_distance > goal_distance:
            return (total_time - press_duration) - press_duration + 1
    return 0


def p1():
    times = nums(lines[0])
    distances = nums(lines[1])
    ans = 1
    for i in range(len(times)):
        ans *= solutions_of(times[i], distances[i])
    print(ans)


def p2():
    long_time = int(lines[0].split(':')[1].replace(' ', ''))
    long_goal = int(lines[1].split(':')[1].replace(' ', ''))
    print(solutions_of(long_time, long_goal))


p1()
p2()
