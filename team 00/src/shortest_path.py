import os
import argparse
import json


def get_database():
    file = os.environ.get('WIKI_FILE', 'wiki.json')
    if not os.path.exists(file):
        print('Database not found')
        exit()
    with open(file, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_shortest_path(database, source, target, non_directed=False):
    short_list = {}
    for entry in database['edges']:
        if entry["from"] not in short_list:
            short_list[entry["from"]] = []
        short_list[entry["from"]].append(entry["to"])
        if non_directed:
            if entry["to"] not in short_list:
                short_list[entry["to"]] = []
            short_list[entry["to"]].append(entry["from"])

    visited = set()
    distances = {source: 0}
    queue = [source]
    while queue:
        current = queue.pop(0)
        if current == target:
            return distances[current]
        visited.add(current)
        for neighbor in short_list.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
    return 'Path not found'


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Find the shortest path between two pages")
    parser.add_argument("--from", dest="source",
                        required=True, help="source page")
    parser.add_argument("--to", dest="target",
                        required=True, help="target page")
    parser.add_argument("--non-directed", action="store_true",
                        help="use bidirectional edges")
    args = parser.parse_args()
    database = get_database()
    shortest_path = get_shortest_path(
        database, args.source, args.target, args.non_directed)
    print(shortest_path)
