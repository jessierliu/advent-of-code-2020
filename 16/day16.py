"""
Day 16
"""

with open('input.txt', 'r') as f:
    lines = f.read()

# parse input
line_split, other_tickets = lines.split('nearby tickets:')
rule_lines, my_ticket = line_split.split('your ticket:')
my_ticket = my_ticket.strip('\n').split(',')
other_tickets = other_tickets.strip('\n').split('\n')

rule_lines = rule_lines.strip('\n').split('\n')
rules = {}
for r in rule_lines:
    key, values = r.split(':')
    values = values.replace(' ', '').split('or')

    rules[key] = []
    for val in values:
        start, stop = val.strip(' ').split('-')
        rules[key].extend(list(range(int(start), int(stop) + 1)))

# part 1: which tickets are invalid
invalid_values = 0
valid_tickets = []
valid_ticket_counts = []
for cur_ticket, ticket in enumerate(other_tickets):

    tix = ticket.split(',')
    tix = [int(t) for t in tix]
    ticket_count = [0 for _ in tix]

    for i, t in enumerate(tix):
        for key in rules.keys():
            if t in rules[key]:
                ticket_count[i] += 1

    if ticket_count.count(0) == 1:
        invalid_values += tix[ticket_count.index(0)]

    elif ticket_count.count(0) >= 1:

        for j, tc in enumerate(ticket_count):
            if tc == 0:
                invalid_values += tix[j]

    else:
        valid_tickets.append(tix)
        valid_ticket_counts.append(ticket_count)

print(invalid_values)

# part 2
bad_fields = [list() for _ in range(len(tix))]
for cur_ticket, tix in enumerate(valid_tickets):

    for i, t in enumerate(tix):
        for key in rules.keys():
            if t not in rules[key]:
                bad_fields[i].append(key)

lengths = [len(i) for i in bad_fields]
available_fields = list(rules.keys())
field_assignment = [None for _ in bad_fields]
for num_bad_fields in reversed(range(len(lengths))):
    idx = lengths.index(num_bad_fields)

    field_assignment[idx] = list(set(available_fields) -
                                 set(bad_fields[idx]))[0]

    available_fields.remove(field_assignment[idx])

dept = 1
for cur_field, field in enumerate(field_assignment):
    if field.startswith('departure'):
        dept *= int(my_ticket[cur_field])

print(dept)
