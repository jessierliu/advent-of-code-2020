"""
Day 7
"""

with open('input.txt', 'r') as f:
    lines = f.read()

lines = lines.split('\n')[:-1]

# build initial dictionary
bag_tree = {}

for line in lines:
    toplevel = line.strip('.').split(' bags contain ')

    bag_tree[toplevel[0]] = {}

    if toplevel[1] == 'no other bags':
        bag_tree[toplevel[0]] = None

    else:
        bag_tree[toplevel[0]] = {}

        for level in toplevel[1].split(', '):
            lowlevel = level.split(' ')
            bag_tree[toplevel[0]][' '.join(lowlevel[1:3])] = int(lowlevel[0])


def get_parents(tree=None, boi=None):
    cont = []
    for b in boi:
        for topkey, topval in tree.items():
            if topval is not None and b in topval.keys():
                cont.append(topkey)
    return cont

# search dict
new = get_parents(tree=bag_tree, boi=['shiny gold'])
total = new.copy()
prev_len = 0

while len(set(total)) != prev_len:
    new = get_parents(tree=bag_tree, boi=new)
    prev_len = len(set(total))
    total.extend(new)

print(len(set(total)))

def get_children(tree=None, boi=None):
    children_keys = []
    total_bags = 0
    for b in boi:
        if isinstance(tree[b], dict):
            for bag_type, bag_count in tree[b].items():
                total_bags += bag_count
                children_keys.extend([bag_type for _ in range(bag_count)])
    return children_keys, total_bags

child_total = 0
new_keys = ['shiny gold']
while len(new_keys) != 0:
    new_keys, new_total = get_children(tree=bag_tree, boi=new_keys)
    child_total += new_total

print(child_total)
