"""Hermetic tests for the drawn glyphs (decision 1680). Needs networkx: run in a
venv with requirements.txt installed; the test never skips on a missing import."""
import struct
import tempfile
import unittest
from collections import Counter
from pathlib import Path

import render

TYPES = list(render.BLOCK_NAMES)  # a name both HEAD and the new code share
FIXTURE = {
    "nodes": [{"id": t, "type": t, "label": t, "tech": "x"} for t in TYPES],
    "edges": [{"from": TYPES[0], "to": t} for t in TYPES[1:]],
}


def _dominant(tile):
    b = tile.tobytes(); px = [tuple(b[i:i + 3]) for i in range(0, len(b), 4) if b[i + 3] == 255]
    return Counter(px).most_common(1)[0][0]


class GlyphTests(unittest.TestCase):
    def test_fixture_covers_ten_types(self):
        self.assertEqual(len(TYPES), 10)
        self.assertEqual(set(render.GLYPH_FILL), set(render.BLOCK_NAMES))

    def test_outline_is_bottom_edge_for_every_type(self):
        old = render.OUTLINE
        render.OUTLINE = "#4a5568"
        render._glyph_cache.clear()  # cache key omits OUTLINE; stale tiles otherwise
        try:
            for t in TYPES:
                tile = render.glyph_tile(t, render.ICON_SIZE)
                x = tile.size[0] // 2
                ys = [y for y in range(tile.size[1]) if tile.getpixel((x, y))[3] > 200]
                px = tile.getpixel((x, max(ys)))[:3]
                self.assertTrue(all(abs(a - b) <= 24 for a, b in zip(px, render._rgb("#4a5568"))), (t, px))
        finally:
            render.OUTLINE = old
            render._glyph_cache.clear()

    def test_smoke_render(self):
        with tempfile.TemporaryDirectory() as d:
            out = Path(d) / "a.png"
            render.render(FIXTURE, str(out))
            self.assertTrue(out.exists())
            self.assertEqual(struct.unpack(">II", out.read_bytes()[16:24]), (580, 3644))  # same as HEAD for this fixture

    def test_tiles_fill_box_with_family_colour(self):
        for size in (render.ICON_SIZE, render.LEGEND_ICON_SIZE):
            for t in TYPES:
                tile = render.glyph_tile(t, size)
                self.assertEqual(tile.size, render.GLYPH_BOX[size], (t, size))
                self.assertEqual(tile.getchannel("A").getbbox(), (0, 0) + tile.size, (t, size))
                fam = render._rgb(render.GLYPH_FILL[t])
                dom = _dominant(tile)
                self.assertTrue(all(abs(a - b) <= 2 for a, b in zip(dom, fam)), (t, size, dom, fam))

    def test_entities_outlined_blocks_flat_by_default(self):
        self.assertIsNone(render.OUTLINE)
        self.assertEqual(render.ENTITY_TYPES, {"user", "external_service", "time"})
        render._glyph_cache.clear()
        edge = render._rgb(render.ENTITY_OUTLINE)
        for size in (render.ICON_SIZE, render.LEGEND_ICON_SIZE):
            for t in TYPES:
                tile = render.glyph_tile(t, size)
                w, h = tile.size
                px = tile.load()
                y = max(y for y in range(h) if px[w // 2, y][3] > 200)
                got = px[w // 2, y][:3]
                want = edge if t in render.ENTITY_TYPES else render._rgb(render.GLYPH_FILL[t])
                self.assertTrue(all(abs(a - b) <= 24 for a, b in zip(got, want)), (t, size, got, want))

    def test_big_tiles_pairwise_distinct(self):
        raw = {t: render.glyph_tile(t, render.ICON_SIZE).tobytes() for t in TYPES}
        self.assertEqual(len(set(raw.values())), len(TYPES))

    def test_unknown_type_and_size_raise(self):
        with self.assertRaises(KeyError):
            render.glyph_tile("nope", render.ICON_SIZE)
        with self.assertRaises(KeyError):
            render.glyph_tile("service", 99)

    def test_no_png_shipped_and_walk_works(self):
        root = Path(render.__file__).parent
        found = [p.name for p in root.rglob("*") if p.is_file()]
        self.assertIn("render.py", found)  # positive control for the walk
        self.assertEqual([n for n in found if n.endswith(".png")], [])

    def test_no_image_open(self):
        for p in Path(render.__file__).parent.rglob("*.py"):
            self.assertEqual(p.read_text().count("Image" + ".open"), 0, p.name)


if __name__ == "__main__":
    unittest.main()
