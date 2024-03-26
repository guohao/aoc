import re
import networkx as nx


def p1(data:str):
    G = nx.Graph()
    for line in data.splitlines():
        cells = re.findall(r'\d+',line)
        frm = cells[0]
        for to in cells[1:]:
            G.add_edge(frm,to)
    return len(nx.node_connected_component(G,'0'))


def p2(data:str):
    G = nx.Graph()
    for line in data.splitlines():
        cells = re.findall(r'\d+',line)
        frm = cells[0]
        for to in cells[1:]:
            G.add_edge(frm,to)
    return len(list(nx.connected_components(G)))
