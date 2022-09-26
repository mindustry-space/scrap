#!/usr/bin/env nix-shell
#!nix-shell -i python3 -p python3Packages.orjson

from pathlib import Path
from orjson import loads

bundles = set()
keys = set()

input = Path("../lead/bundles")
output = Path("./bundles")

for v in input.glob("*.json"):
    data = loads(v.read_text())
    bundles.update(data.keys())
    for v in data.values():
        keys.update(v.keys())

output.mkdir(exist_ok=True)
for v in output.glob("*.properties"):
    v.unlink()

keys = list(keys)
keys.sort()
keys = filter(lambda k: not k.startswith("#"), keys)
bundle = "\n".join(map(lambda k: f"{k} = {k}", keys))

for v in bundles:
    (output / v).write_text(bundle)
