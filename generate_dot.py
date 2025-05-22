#!/usr/bin/env python3
import sys

def parse_nodes(file_path):
    nodes = []
    edges = []
    parents = {}
    counter = 0
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            indent = len(line) - len(line.lstrip(' '))
            label = line.strip()
            if not label:
                continue
            if indent == 0:
                level = 0
            elif indent == 4:
                level = 1
            elif indent == 8:
                level = 2
            elif indent == 12:
                level = 3
            else:
                continue
            node_id = f'n{counter}'
            nodes.append((node_id, label))
            if level > 0:
                parent_id = parents[level-1]
                edges.append((parent_id, node_id))
            parents[level] = node_id
            counter += 1
    return nodes, edges

def write_dot(nodes, edges, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('digraph KnowledgeGraph {\n')
        f.write('  graph [overlap=false];\n')
        f.write('  node [shape=box, fontname=\"Arial\"];\n')
        for node_id, label in nodes:
            safe = label.replace('"', '\"')
            f.write(f'  {node_id} [label=\"{safe}\"];\n')
        for u, v in edges:
            f.write(f'  {u} -> {v};\n')
        f.write('}\n')

def main():
    if len(sys.argv) != 3:
        print("Usage: generate_dot.py knowledge_nodes.txt output.dot")
        sys.exit(1)
    nodes, edges = parse_nodes(sys.argv[1])
    write_dot(nodes, edges, sys.argv[2])

if __name__ == "__main__":
    main()
