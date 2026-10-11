# Recoloured copy of split_CombFigr_0site2r0_grid.pdf (draft Fig. 5) for the talk.
# The original runs from blue (J = 1) to red (J = 10), which clashes with the deck's regime colours
# (blue = Kondo, red = free moment). Here J = 1 is the AFM green and J = 10 the Kondo blue.
# Only the five stroke colours are swapped; the original file is not touched.
# Run: ~/anaconda3/bin/python make_fig5_regime_colours.py
import re, zlib

SRC, DST = "split_CombFigr_0site2r0_grid.pdf", "fig5_regime_colours.pdf"
SWAP = {  # original r g b  ->  new (R, G, B) in 0..255
    b"0.1294117647 0.4 0.6745098039": (46, 139, 87),            # J = 1: AFM green
    b"0.2931180315 0.5956939639 0.7750865052": (120, 185, 150),  # J = 3
    b"0.6287240878 0.7604740049 0.8049631556": (165, 180, 195),  # J = 5
    b"0.9104805844 0.3298885044 0.2179623222": (120, 150, 240),  # J = 8
    b"0.6470588235 0 0.1490196078": (40, 80, 230),              # J = 10: Kondo blue
}
SWAP = {k: b"%.4f %.4f %.4f" % tuple(c / 255 for c in v) for k, v in SWAP.items()}

data = open(SRC, "rb").read()
objs = {int(m.group(1)): m.group(2) for m in re.finditer(rb"(\d+) 0 obj(.*?)endobj", data, re.S)}
nswap = 0
for num, body in list(objs.items()):
    m = re.match(rb"(.*?)stream\r?\n(.*?)\r?\nendstream", body, re.S)
    if not m or b"FlateDecode" not in m.group(1):
        continue
    try:
        s = zlib.decompress(m.group(2))
    except zlib.error:
        continue
    new = s
    for old, col in SWAP.items():
        new, n = re.subn(re.escape(old) + rb"(?= (RG|rg)\b)", col, new)
        nswap += n
    if new == s:
        continue
    comp = zlib.compress(new)
    head = m.group(1)
    ref = re.search(rb"/Length (\d+) 0 R", head)
    if ref:                                   # length stored in another object
        objs[int(ref.group(1))] = b"\n%d\n" % len(comp)
    else:
        head = re.sub(rb"/Length \d+", b"/Length %d" % len(comp), head)
    objs[num] = head + b"stream\n" + comp + b"\nendstream\n"
assert nswap == 21, nswap                     # 6 + 3 + 3 + 3 + 6 strokes in the original

out = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
offs = {}
for num in sorted(objs):
    offs[num] = len(out)
    out += b"%d 0 obj" % num + objs[num] + b"endobj\n"
size = max(objs) + 1
xref = len(out)
out += b"xref\n0 %d\n0000000000 65535 f \n" % size
for num in range(1, size):
    out += b"%010d 00000 n \n" % offs[num] if num in offs else b"0000000000 65535 f \n"
trailer = re.search(rb"trailer\s*<<(.*?)>>", data, re.S).group(1)
trailer = re.sub(rb"/Size \d+", b"/Size %d" % size, trailer)
out += b"trailer\n<<" + trailer + b">>\nstartxref\n%d\n%%%%EOF\n" % xref
open(DST, "wb").write(out)
print("wrote", DST, "with", nswap, "colours swapped")
