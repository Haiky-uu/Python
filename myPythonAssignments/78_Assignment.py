# 78 read the testDuplicate file and find duplicate lines in file

dup = set()
all = set()

for line in open("./testDuplicate", 'r'):
    strip_line = line.strip()
    if strip_line in all:
        dup.add(strip_line)
    else:
        all.add(strip_line)

for d in dup:
    print(d)