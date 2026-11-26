import sys
import tree_sitter_python as tspython
from tree_sitter import Language, Parser

parser = Parser(Language(tspython.language()))

def jelajah(node, kedalaman=0, field=None):
    baris, kolom = node.start_point
    label = f"{field}: " if field else ""
    print("  " * kedalaman + f"{label}{node.type} [{baris + 1}:{kolom}]")
    
    for i, child in enumerate(node.children):
        if not child.is_named:
            continue
        nama_field = node.field_name_for_child(i)
        jelajah(child, kedalaman + 1, nama_field)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Pemakaian: python jelajah.py <file.py>")
        sys.exit(1)
    with open(sys.argv[1], "rb") as f:
        tree = parser.parse(f.read())
    jelajah(tree.root_node)
