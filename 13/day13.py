"""
Day 13
"""

with open('input.txt', 'r') as f:
    lines = f.read()

my_time, buses = lines.strip('\n').split('\n')
my_time = int(my_time)
buses = buses.split(',')
valid_buses = [int(bus) for bus in buses if bus != 'x']

# part 1
next_times = [bus - (my_time % bus) for bus in valid_buses]
print(valid_buses[next_times.index(min(next_times))] * min(next_times))

data = open('input.txt', 'r').read().split('\n')
data = data[1].split(',')
B = [(int(data[k]), k) for k in range(len(data)) if data[k] != 'x']

# part 2
rel_assignment = [i for i, bus in enumerate(buses) if bus != 'x']

lcm, cur_time = 1, 0
for i in range(len(valid_buses) - 1):

    bus = valid_buses[i + 1]
    rel = rel_assignment[i + 1]
    lcm *= valid_buses[i]

    while (cur_time + rel) % bus != 0:
        cur_time += lcm

print(cur_time)
