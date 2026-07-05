"""Build a myst_sphinx_gallery tree from example notebooks."""

from __future__ import annotations

import hashlib
import json
import re
import shutil
from pathlib import Path
import nbformat

# Config

ExamplesRoot = Path("~/online/benchmarks/benchmarks/").expanduser()
OutputRoot = Path(__file__).parent.parent/"gallery2"
OutputDocs = Path(__file__).parent/"examples/"

Galleries = [
    {
        "name": "General",
        "directory": "general",
        "description": "General examples.",
        "examples": [
            # "node-0005/a.ipynb",
            "solve-0003/main.ipynb",
            "model-0001/model-0001.ipynb"
        ],
    },
    {
        "name": "Frames",
        "directory": "frames",
        "description": "Frame examples.",
        "examples": [
            "frame-0059/main.ipynb",
            "frame-2005/frame-2005.ipynb",
            # "frame-1010/main.ipynb",
            "frame-3056/main.ipynb",
        ],
    },
    {
        "name": "Sections",
        "directory": "sections",
        "description": "Section examples.",
        "examples": [
            "fiber-0002/fiber-0002.ipynb",
            "fiber-0003/fiber-0003.ipynb",
            "fiber-0004/fiber-0004.ipynb",
        ],
    },
    {
        "name": "Plane Elasticity",
        "directory": "plane",
        "description": "Plane examples.",
        "examples": [
            "plane-0002/main.ipynb",
            "plane-0101/main.ipynb",
            "plane-2001/main.ipynb",
        ],
    },
    {
        "name": "Material",
        "directory": "material",
        "description": "Material examples.",
        "examples": [
            "material-0002/main.ipynb",
            "material-0003/main.ipynb",
            "material-0004/main.ipynb",
            "material-0011/main.ipynb",
            "material-0012/main.ipynb",
            "material-0005/main.ipynb",
            "material-0030/main.ipynb",
            "material-0031/main.ipynb",
            "model-5012/main.ipynb",
            "solid-0203/main.ipynb",
        ],
    },
    {
        "name": "Nonlinear Geometry",
        "directory": "geometry",
        "description": "Nonlinear geometry.",
        "examples": [
            "frame-1010/frame-1010.ipynb",
        ],
    },
]

#
# Helpers
#

HASH_LEN = 8


def short_hash(s: str) -> str:
    return hashlib.sha256(s.encode()).hexdigest()[:HASH_LEN]


def collect_image_renames(src_img_dir: Path, rel_nb_path: str) -> dict[str, str]:
    """{original_basename -> hashed_basename} for one example's img/ dir.

    Hash input includes the notebook's relative path so the same image
    name across two examples gets two distinct hashes, and so rebuilds
    are deterministic.
    """
    rename_map: dict[str, str] = {}
    if not src_img_dir.is_dir():
        return rename_map
    for img in sorted(src_img_dir.iterdir()):
        if not img.is_file():
            continue
        h = short_hash(f"{rel_nb_path}::img/{img.name}")
        rename_map[img.name] = f"{img.stem}-{h}{img.suffix}"
    return rename_map


def rewrite_image_refs(source, rename_map: dict[str, str], gallery_img_dir: Path):
    """Rewrite `img/<old>` -> `img/<new>` in a notebook cell source.

    Cell source can be a list[str] or str per nbformat; we handle both.
    """
    if not rename_map:
        return source
    keys = sorted(rename_map, key=len, reverse=True)
    pattern = re.compile(r"img/(" + "|".join(re.escape(k) for k in keys) + r")")

    def repl(m: re.Match) -> str:
        # return f"img/{rename_map[m.group(1)]}"
        return f"/{gallery_img_dir/rename_map[m.group(1)]}"
        # return f"{rename_map[m.group(1)]}"

    if isinstance(source, str):
        return pattern.sub(repl, source)
    return [pattern.sub(repl, line) for line in source]


def write_gallery_header(gallery_dir: Path, gallery: dict) -> None:
    name = gallery["name"]
    description = (gallery.get("description") or "").strip()
    body = f"{name}\n{'=' * len(name)}\n"
    if description:
        body += f"\n{description}\n"
    (gallery_dir / "GALLERY_HEADER.rst").write_text(body)


# Main copy logic


# def process_example(
#     rel_nb_path: str,
#     examples_root: Path,
#     gallery_dir: Path,
#     gallery_img_dir: Path,
#     used_dest_names: set[str],
# ) -> None:
#     src_nb = examples_root / rel_nb_path
#     if not src_nb.is_file():
#         raise FileNotFoundError(f"Notebook not found: {src_nb}")

#     example_key = Path(rel_nb_path).parts[0]
#     if example_key in used_dest_names:
#         raise ValueError(
#             f"Duplicate example key '{example_key}' in gallery '{gallery_dir.name}'"
#         )
#     used_dest_names.add(example_key)

#     src_example_dir = src_nb.parent

#     rename_map = collect_image_renames(src_example_dir / "img", rel_nb_path)
#     for old_name, new_name in rename_map.items():
#         shutil.copy2(src_example_dir / "img" / old_name, gallery_img_dir / new_name)

#     nb = json.loads(src_nb.read_text())
#     for cell in nb.get("cells", []):
#         if cell.get("cell_type") in ("markdown", "code"):
#             cell["source"] = rewrite_image_refs(cell.get("source", []), rename_map)

#     dest_nb = gallery_dir / f"{example_key}.ipynb"
#     dest_nb.write_text(json.dumps(nb, indent=1, ensure_ascii=False))
#     print(f"  {rel_nb_path} -> {dest_nb.relative_to(gallery_dir.parent)}")


def process_example(
    rel_nb_path: str,
    examples_root: Path,
    gallery_dir: Path,
    gallery_img_dir: Path,
    used_dest_names: set[str],
) -> None:
    src_nb = examples_root / rel_nb_path
    if not src_nb.is_file():
        raise FileNotFoundError(f"Notebook not found: {src_nb}")

    example_key = Path(rel_nb_path).parts[0]
    if example_key in used_dest_names:
        raise ValueError(
            f"Duplicate example key '{example_key}' in gallery '{gallery_dir.name}'"
        )
    used_dest_names.add(example_key)

    src_example_dir = src_nb.parent

    rename_map = collect_image_renames(src_example_dir / "img", rel_nb_path)
    for old_name, new_name in rename_map.items():
        shutil.copy2(src_example_dir / "img" / old_name, 
                     gallery_img_dir / new_name)

    # changed: read/write through nbformat instead of raw json
    nb = nbformat.read(src_nb, as_version=4)
    # add download button
    # download_md = (
    #     f"{{download}}`Download <{example_key}.ipynb>`"
    # )
    # nb.cells.insert(1, nbformat.v4.new_markdown_cell(download_md))
    # process images
    for cell in nb.cells:
        if cell.cell_type in ("markdown", "code"):
            cell.source = rewrite_image_refs(cell.source, rename_map, gallery_img_dir)
        if cell.cell_type == "code" and "#<hide>" in cell.source:
            cell.source = ""
            cell.cell_type = "markdown"

    dest_nb = gallery_dir / f"{example_key}.ipynb"
    nbformat.write(nb, dest_nb)
    #

    print(f"  {rel_nb_path} -> {dest_nb.relative_to(gallery_dir.parent)}")


def build(output_root: Path) -> None:
    output_root.mkdir(parents=True, exist_ok=True)
    for gallery in Galleries:
        gallery_dir = output_root / gallery["directory"]
        if gallery_dir.exists():
            shutil.rmtree(gallery_dir)
        gallery_dir.mkdir(parents=True)

        # gallery_img_dir = gallery_dir #/ "img"
        # gallery_img_dir.mkdir()
        gallery_img_dir = Path("_static")/"images"/"gallery"

        print(f"[{gallery['name']}] -> {gallery_dir}")
        write_gallery_header(gallery_dir, gallery)

        used: set[str] = set()
        for example_rel in gallery["examples"]:
            process_example(
                rel_nb_path=example_rel,
                examples_root=ExamplesRoot,
                gallery_dir=gallery_dir,
                gallery_img_dir=gallery_img_dir,
                used_dest_names=used,
            )


if __name__ == "__main__":
    build(OutputRoot)
