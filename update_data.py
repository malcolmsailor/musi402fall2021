#!/usr/bin/env python3

import os
import re
import sys

import yaml

"""First argument should be "sketches", "handouts" or "assignments."
"""

COURSE_DIR = "/Users/Malcolm/Courses/2021_02_tonal_counterpoint"

try:
    subdir = sys.argv[1]
except:
    print("sys.argv[1] must be in 'handouts', 'assignments', 'sketches'")
    sys.exit(1)

dir = os.path.join(COURSE_DIR, subdir)

out = []

for basename in os.listdir(dir):
    if basename.startswith("_"):
        continue
    if basename.endswith(".md"):
        with open(os.path.join(dir, basename), "r", encoding="utf-8") as inf:
            front_matter = next(yaml.load_all(inf, Loader=yaml.FullLoader))
        front_matter["basename"] = basename[:-3] + ".pdf"
        out.append(front_matter)
    if subdir == "sketches" and basename.endswith(".pdf"):
        # should be a sketch, with following naming format:
        # [assignment_no]_[date, separated by underscores].pdf
        m = re.match(r"^(\d+)_(.*)\.pdf", basename)
        assignment_no = m.groups()[0]
        date = m.groups()[1].replace("_", " ")
        front_matter = {
            "assignment_no": assignment_no,
            "date": date,
            "basename": basename,
        }
        out.append(front_matter)

SORT_KEYS = {
    "handouts": "handout_no",
    "assignments": "assignment_no",
    "sketches": "assignment_no",
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
