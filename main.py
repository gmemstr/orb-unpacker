#!/usr/bin/python
# Splits arbitrary orb.yml files into destructured versions.
import yaml
import sys
from pathlib import Path

orb = {}
meta = {}
directories = ["executors", "jobs", "commands", "examples"]
with open(sys.argv[1]) as orbfile:
    orb = yaml.load(orbfile)

for thing in orb:
    if thing in directories:
        Path("./out/" + thing).mkdir(parents=True, exist_ok=True)
        for subthing in orb[thing]:
            f = open("./out/" + thing + "/" + subthing + ".yml", "w+")
            yaml.dump(orb[thing][subthing], f, default_flow_style=False)
    else:
        meta[thing] = orb[thing]

f = open("./out/@orb.yml", "w+")
yaml.dump(meta, f, default_flow_style=False)
