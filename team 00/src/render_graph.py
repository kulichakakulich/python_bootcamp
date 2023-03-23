import os
import json
import networkx as nx
import matplotlib.pyplot as plt


def get_database():
    try:
        file = os.environ.get('WIKI_FILE', 'wiki.json')
        with open(file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except KeyError:
        print('Database not found')


if __name__ == "__main__":

    data = get_database()

    G = nx.DiGraph()
    nodes_list = [i['name_page'] for i in data['nodes']]
    edges_list = [(i['from'], i['to']) for i in data['edges']]
    G.add_nodes_from(nodes_list)
    G.add_edges_from(edges_list)

    plt.figure(figsize=(30, 30))
    list_degree = G.degree()  # this will return a list of tuples each tuple is(node,deg)
    nodes, degree = map(list, zip(*list_degree))  # build a node list and corresponding degree list
    nx.draw(G, with_labels=True, nodelist=nodes_list, node_size=[(v * 100) + 1 for v in degree])
    plt.axis('off')
    plt.savefig('wiki_graph.png')
    plt.show()
