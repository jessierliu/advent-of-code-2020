"""
Day 19
"""
import regex

with open('input.txt', 'r') as f:
    lines = f.read()

rule_lines, messages = lines.strip('\n').split('\n\n')
rule_lines = rule_lines.split('\n')
messages = messages.split('\n')

rules = {}
for r in rule_lines:
    num, content = r.strip(' ').split(': ')
    rules[num] = content.replace('"', '')


def match_zero(rules, messages):
    def expand(word):
        return rule(word) if word.isdigit() else word

    def rule(roi):
        return '(?:' + ''.join(map(expand, rules[roi].split(' '))) + ')'

    reg = regex.compile(rule('0'))
    matches = [True if reg.fullmatch(m) else False for m in messages]
    return sum(matches)


print(match_zero(rules, messages))

# change
# todo, don't understand the rule 11 change still
# 8: 42 | 42 8  --> as many 42's as possible
# 11: 42 31 | 42 11 31
rules['8'] = '42 +'
rules['11'] = '(?P<group> 42 (?&group)? 31 )'
print(match_zero(rules, messages))
