"""Tugas 3 — Penjalan query: jalankan file .scm pada file Python."""

import sys
import tree_sitter_python as tspython
from tree_sitter import Language, Parser, Query, QueryCursor

PY = Language(tspython.language())
parser = Parser(PY)

if len(sys.argv) < 3:
    print("Pemakaian: python q.py <file.py> <query.scm>")
    sys.exit(1)

kode = open(sys.argv[1], "rb").read()
pola = open(sys.argv[2]).read()
tree = parser.parse(kode)

hasil = QueryCursor(Query(PY, pola)).captures(tree.root_node)
for nama, nodes in hasil.items():
    for n in nodes:
        print(f"@{nama}  baris {n.start_point[0] + 1}: {n.text.decode()}")
