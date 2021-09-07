# Uses python3
import sys


def compute_min_refills(distance, tank, stops):
    full_tank = tank
    count = 0
    prev_stop = 0
    if (distance - tank) < 0:
        return 0
    for stop in stops:
        stop = float(stop)
        dis = stop - prev_stop
        if dis > tank and dis > full_tank:
            return -1
        else:
            if dis > tank:
                tank = full_tank
                count += 1
            tank = tank - dis
            prev_stop = stop

    distance = distance - stop
    if (distance - tank) <= 0:
        return count
    else:
        if distance > full_tank:
            return -1
        else:
            return count + 1

d = int(input())
m = int(input())
n = int(input())
stops = input().split()

print(int(compute_min_refills(d, m, stops)))
