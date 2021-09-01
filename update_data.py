#!/usr/bin/env python3

import os
import sys

import yaml

"""First argument should be "handouts" or "assignments."
"""

COURSE_DIR = "/Users/Malcolm/Courses/2021_02_tonal_counterpoint"

try:
    subdir = sys.argv[1]
except:
    print("sys.argv[1] must be in 'handouts', 'assignments'")
    sys.exit(1)

dir = os.path.join(COURSE_DIR, subdir)

out = []

for basename in os.listdir(dir):
    if basename.startswith("_") or not basename.endswith(".md"):
        continue
    with open(os.path.join(dir, basename), "r", encoding="utf-8") as inf:
        front_matter = next(yaml.load_all(inf, Loader=yaml.FullLoader))
    front_matter["basename"] = basename[:-3] + ".pdf"
    out.append(front_matter)

SORT_KEYS = {
    "handouts": "handout_no",
    "assignments": "assignment_no",
}

out.sort(key=lambda x: x[SORT_KEYS[sys.argv[1]]])

out_path = os.path.join(
    os.path.dirname((os.path.realpath(__file__))),
    "_data",
    f"{sys.argv[1]}.yml",
)
with open(out_path, "w", encoding="utf-8") as outf:
    yaml.dump(out, outf)
    print(f"Wrote {out_path}")
