from collections import defaultdict

from helper import *

data = raw_data(2017, 7)


class Node:
    def __init__(self, name, v, children=None):
        self.name = name
        self.v = v
        self.children = children or []

    def __str__(self):
        return f'{self.name} {self.v} {self.children}'

    def __repr__(self):
        return self.__str__()


def p1():
    d = {}
    for line in lines(data):
        children = []

        if '->' not in line:
            name, weight = line.split()
        else:
            l, r = line.split('->')
            name, weight = l.split()
            if r is not None:
                cs = r.replace(',', '').split()
                for c in cs:
                    if c not in d:
                        d[c] = Node(c, -1)
                    children.append(d[c])

        weight = int(weight.replace('(', '').replace(')', ''))
        if name in d:
            d[name].children = children
            d[name].v = weight
        else:
            d[name] = Node(name, weight, children)
    for k in set(d.values()):
        for child in k.children:
            d.pop(child.name)
    return list(d.values())[0]


def p2():
    root = p1()

    def weight_of(node) -> int:
        if len(node.children) == 0:
            return node.v
        return node.v + sum(weight_of(c) for c in node.children)

    def find_wrong_weight(node):
        if len(node.children) == 0:
            return None
        for c in node.children:
            ww = find_wrong_weight(c)
            if ww is not None:
                return ww

        cws = [weight_of(c) for c in node.children]
        wd = set(cws)
        if len(wd) == 1:
            return None
        counts = [(cws.count(x), x) for x in wd]
        if len(counts) != 2:
            raise Exception(node.children[cws.index(counts[0][1])].v - (counts[0][1] - counts[1][1]))
        if counts[0][0] > counts[1][0]:
            return node.children[cws.index(counts[1][1])].v + (counts[0][1] - counts[1][1])
        else:
            return node.children[cws.index(counts[0][1])].v + (counts[1][1] - counts[0][1])

    return find_wrong_weight(root)


print(p1().name)
print(p2())
