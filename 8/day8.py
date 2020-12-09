"""
Day 8
"""

with open('input.txt', 'r') as f:
    lines = f.read()
    lines = lines.strip('\n').split('\n')


def acc_val(ops=None, acc=0, op_idx=0, valid_op=True):
    all_ops = [0 for _ in range(len(ops))]
    all_ops[0] = 1

    while all_ops.count(2) == 0 and valid_op:
        line_split = ops[op_idx].split(' ')
        if line_split[0] == 'acc':
            acc += eval(line_split[1])
            op_idx += 1
        elif line_split[0] == 'nop':
            op_idx += 1
        else:
            op_idx += eval(line_split[1])

        if op_idx == len(ops):
            valid_op = False
        else:
            all_ops[op_idx] += 1

    return acc, all_ops.count(2)


print(acc_val(ops=lines)[0])

for cur_line, line in enumerate(lines):

    if line.startswith('jmp'):
        ops_copy = lines.copy()
        ops_copy[cur_line] = line.replace('jmp', 'nop')
    elif line.startswith('nop'):
        ops_copy = lines.copy()
        ops_copy[cur_line] = line.replace('nop', 'jmp')
    else:
        continue

    new_acc, ops_count = acc_val(ops=ops_copy)

    if ops_count == 0:
        print(new_acc)
        break
