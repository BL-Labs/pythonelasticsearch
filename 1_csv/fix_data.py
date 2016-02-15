import csv

from patch import get_lookup_dictionary

# NB like patch.py file, there are two deliberate mistakes in this file.
# it will not work until these are fixed, as well as patch.py working!

SOURCE = "broken_data.csv"
OUTPUT = "fixed_data.csv"

titles = get_lookup_dictionary()

with open(SOURCE) as src:
  with open(OUTPUT, "w") as out:
    s = csv.DictReader(src)
    # Create a DictWriter, setting in place the headers that will be used
    o = csv.DictWriter(out, fieldnames=["sysnum","author","date","place"])
    # Write out the header names:
    o.writerow(dict([(x,x) for x in ["sysnum","author","date","place"]]))
    for row in s:
      # assign the title to be the one from the patch data
      row['title'] = title[row['sysnum']]
      o.writerow(row)

