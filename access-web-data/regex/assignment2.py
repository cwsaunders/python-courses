import re
import os

scriptdir = os.path.dirname(os.path.abspath(__file__))

sp_file = os.path.join(scriptdir, "read.txt")

with open(sp_file) as f:
    content = f.readlines()
y = []

for line in content:
    y.append(re.findall('[0-9]+',line))

print(y)
