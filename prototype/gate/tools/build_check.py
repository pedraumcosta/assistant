"""Runs inside the verdict container: does the change still parse and import?

    python build_check.py <tree hash of the change> <package> [<package> ...]

Exit 0 when it does, 1 with the first reason when it does not, and 3 when the
container does not see the change it was asked to judge.
"""
import ast
import hashlib
import importlib
import pathlib
import sys

root = pathlib.Path("/work")


def tree_hash() -> str:
    """The same hash the host computes (runner/change.py), computed on what this container sees."""
    out, stack = {}, [root]
    while stack:
        for p in sorted(stack.pop().iterdir()):
            rel = p.relative_to(root).as_posix()
            if p.is_symlink():
                out[rel] = "symlink:" + str(p.readlink())
            elif p.is_dir():
                if p.name not in ("__pycache__", ".pytest_cache"):
                    stack.append(p)
            elif not p.name.endswith(".pyc"):
                out[rel] = hashlib.sha256(p.read_bytes()).hexdigest()
    h = hashlib.sha256()
    for rel, digest in sorted(out.items()):
        h.update(f"{rel}\0{digest}\n".encode())
    return h.hexdigest()


expected, packages = sys.argv[1], sys.argv[2:]
if tree_hash() != expected:
    # The container is not looking at the change the verdict is about.
    print("the mounted change is not the change to be judged")
    sys.exit(3)
for path in sorted(root.rglob("*.py")):
    try:
        ast.parse(path.read_text(), str(path))
    except (SyntaxError, UnicodeDecodeError) as e:
        print(f"{path.relative_to(root)} does not parse: {e}")
        sys.exit(1)
sys.path.insert(0, str(root))
for package in packages:
    if not (root / package).is_dir():
        print(f"package {package} is missing")
        sys.exit(1)
    for path in sorted((root / package).rglob("*.py")):
        module = ".".join(path.relative_to(root).with_suffix("").parts).removesuffix(".__init__")
        try:
            importlib.import_module(module)
        except BaseException as e:
            print(f"{module} does not import: {type(e).__name__}: {e}")
            sys.exit(1)
print("BUILD-OK")
