import tree_sitter_python as tspython
from tree_sitter import Language, Parser

parser = Parser(Language(tspython.language()))
# kode = b"x = 1\n"
# tree = parser.parse(kode)
# print(tree.root_node)

potongan = {
    "fungsi": b"""def sapa(nama):
    return "Halo " + nama
""",
    "if_else": b"""x = 10
if x > 5:
    print("besar")
else:
    print("kecil")
""",
    "kelas": b"""class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def suara(self):
        return "..."
""",
}

print("=" * 60)
print("BAGIAN A: Pohon hasil parse (S-expression)")
print("=" * 60)
for label, kode in potongan.items():
    tree = parser.parse(kode)
    print(f"\n--- {label} ---")
    print(tree.root_node)

print("\n" + "=" * 60)
print("BAGIAN B: Error recovery — kode rusak (hapus ':')")
print("=" * 60)
kode_rusak = b"""def sapa(nama)
    return "Halo " + nama
"""
tree_rusak = parser.parse(kode_rusak)
print(tree_rusak.root_node)
def cari_error(node, depth=0):
    if node.is_error or node.is_missing:
        label = "ERROR" if node.is_error else "MISSING"
        print(f"  {'  ' * depth}[{label}] type={node.type} baris={node.start_point[0]+1}")
    for c in node.children:
        cari_error(c, depth + 1)

cari_error(tree_rusak.root_node)
