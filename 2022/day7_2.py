import re


class Node:
    def __init__(self, name, size=0):
        self.name = name
        self.size = size
        self.children = []

def calculate_size(node):
    total_size = node.size
    for child in node.children:
        total_size += calculate_size(child)
    return total_size

data = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
""".strip().split('\n')

nodes = {'/': Node('/')}
current_dir = '/'
for line in data:
    if line.startswith('$ cd '):
        dir_name = line.split()[2]
        if dir_name == '..':
            current_dir = '/'.join(current_dir.split('/')[:-1]) or '/'
        elif dir_name == '/':
            current_dir = '/'
        else:
            if current_dir == '/':
                current_dir = ''
            current_dir = current_dir + '/' + dir_name if current_dir != '/' else current_dir + dir_name
    elif line.startswith('dir '):
        dir_name = line.split()[1]
        if current_dir == '/':
            current_dir = ''
        nodes[current_dir + '/' + dir_name] = Node(dir_name)
        nodes[current_dir].children.append(nodes[current_dir + '/' + dir_name])
    elif re.match(r'\d+', line):
        file_size, file_name = line.split()
        nodes[current_dir].children.append(Node(file_name, int(file_size)))

total_sizes = [calculate_size(node) for node in nodes.values() if calculate_size(node) <= 100000]
print(sum(total_sizes))