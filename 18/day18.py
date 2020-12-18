"""
Day 18
"""

with open('input.txt', 'r') as f:
    lines = f.read()

lines = lines.strip('\n').split('\n')


def new_math(expr):
    """
    expr should be a string, no parens
    """
    expr = expr.split(' ')
    cur_value = expr[0]
    for i in range(1, len(expr), 2):
        cur_value = eval(f'{cur_value} {expr[i]} {expr[i + 1]}')
    return cur_value


def advanced_math(expr):
    """
    expr should be a string, no parens
    """
    while expr.count('+') != 0:

        expr_split = expr.split(' ')
        op = expr_split.index('+')
        to_eval = f'{expr_split[op - 1]} {expr_split[op]} {expr_split[op + 1]}'
        new_value = eval(to_eval)

        if expr.count(to_eval) != 1:
            del expr_split[op + 1], expr_split[op]
            expr_split[op - 1] = str(new_value)
            expr = ' '.join(expr_split)
        else:
            expr = expr.replace(to_eval, str(new_value))

    return eval(expr)


def find_parens(expr):
    """
    expr should be a string
    """
    inds = [None, None]
    for cur, s in enumerate(expr):
        if s == '(':
            inds = [cur, None]
        elif s == ')' and inds[1] is None:
            inds[1] = cur
    return inds


def reduce_parens(expr, fcn=None):
    """
    expr should be a string
    """
    idx = find_parens(expr)
    new_value = fcn(expr[idx[0] + 1:idx[1]])
    expr = expr.replace(str(expr[idx[0]:idx[1] + 1]), str(new_value))
    return expr


# part 1
total = 0
for line in lines:
    while line.count('(') != 0:
        line = reduce_parens(line, fcn=new_math)
    total += new_math(line)

print(total)

# part 2
total = 0
for line in lines:
    while line.count('(') != 0:
        line = reduce_parens(line, fcn=advanced_math)
    total += advanced_math(line)

print(total)
