"""
csv2json.py -> transform excel CSV into web-ready JSON
anonymize & randomize data as necessary
"""

import csv
import json
import random
import sys

USAGE = "python csv2json.py ORIGINAL.csv WEBREADY.json\n"

if len(sys.argv) != 3:
    print USAGE
    sys.exit(1)
infile = sys.argv[1]
outfile= sys.argv[2]


# Opt-in: these are the cells to include
COLS = ["DR#", "Dispatch Date", "City", "Incident Type", "Zip Code", "County",
        "Dispatch Time", "Call Out Person",
        "Time to Find Responders", "Time Responders on Scene",
        "Responder #1", "Responder #2", "Responder #3",
        "Responder #4", "Responder #5", "Responder #6",
        "Adults", "Children",
        "C-Kits", "Bears", "Toys", "Water", "Snacks", "Prepacks", "Blanket",
        "Meals", "Shelter", "Misc"]

# Only include first-names for values in the following columns
FIRST_NAME = ["Responder #1", "Responder #2", "Responder #3",
              "Responder #4", "Responder #5", "Responder #6"]

# Make junk values here (no relation to source data)
RANDOMIZE = ["Time to Find Responders", "Time Responders on Scene"]

reader = csv.reader(open(infile))

colnames = reader.next()

out = []
for row in reader:
    obj = {}
    for idx, col in enumerate(row):
        name = colnames[idx]
        if name in COLS:
            if name in FIRST_NAME:
                col = col.split(" ")[0]
            elif name in RANDOMIZE:
                col = random.randint(0,120)
            obj[name] = col
    out.append(obj)

json.dump(out, open(outfile, 'w'), indent=2)
