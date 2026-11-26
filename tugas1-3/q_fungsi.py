"""Tugas 3 — Query dengan matches: nama fungsi + jumlah parameter."""

import sys
import tree_sitter_python as tspython
from tree_sitter import Language, Parser, Query, QueryCursor

PY = Language(tspython.language())
parser = Parser(PY)

kode = open(sys.argv[1], "rb").read()
tree = parser.parse(kode)

pola = "(function_definition name: (identifier) @nama parameters: (parameters) @params)"
for _, cap in QueryCursor(Query(PY, pola)).matches(tree.root_node):
    nama = cap["nama"][0].text.decode()
    jumlah = cap["params"][0].named_child_count
    print(f"{nama}  ({jumlah} parameter)")
