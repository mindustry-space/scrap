#!/usr/bin/env python
from pathlib import Path


for bundle in Path("../Mindustry/core/assets/bundles").glob("*.properties"):
    new = []

    with open(bundle) as file:
        for line in file.readlines():
            if " = " not in line: 
                continue
            key = line.split(" = ")[0]
            new.append(f"{key} = {key}\n")

    with open(Path("bundles") / bundle.name, "w") as file:
        file.writelines(new)

