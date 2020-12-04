"""
Day 4
"""

import re


def special_match(string, search=re.compile(r'[^a-f0-9.]').search):
    return not bool(search(string))


with open('input.txt', 'r') as f:
    lines = f.read()

lines = lines.split('\n\n')

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
optional = 'cid'
valid, super_valids, checks = 0, 0, 0

for cur_line in lines:
    entry = cur_line.strip('\n').strip(' ').replace('\n', ' ').split(' ')
    fields = [e.split(':')[0] for e in entry]
    values = [e.split(':')[1] for e in entry]
    fields_copy = fields.copy()

    if optional in fields:
        fields_copy.remove(optional)

    if sorted(fields_copy) == sorted(required_fields):
        valid += 1

        for req in required_fields:
            idx = fields.index(req)

            if req == 'byr' and 1920 <= int(values[idx]) <= 2002:
                checks += 1
            elif req == 'iyr' and 2010 <= int(values[idx]) <= 2020:
                checks += 1
            elif req == 'eyr' and 2020 <= int(values[idx]) <= 2030:
                checks += 1
            elif req == 'hgt':
                if values[idx].endswith('cm') and 150 <= int(
                        values[idx].strip('cm')) <= 193:
                    checks += 1
                elif values[idx].endswith('in') and 59 <= int(
                        values[idx].strip('in')) <= 76:
                    checks += 1
            elif req == 'hcl' and values[idx][0] == '#' and \
                    len(values[idx][1:]) == 6 and special_match(
                values[idx][1:]):
                checks += 1
            elif req == 'ecl' and values[idx] in ['amb', 'blu', 'brn',
                                                  'gry', 'grn', 'hzl', 'oth']:
                checks += 1
            elif req == 'pid' and len(values[idx]) == 9:
                checks += 1
            else:
                break

        if checks == 7:
            super_valids += 1

        checks = 0

print(valid)
print(super_valids)
