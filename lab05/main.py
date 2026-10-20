from tablestats import *
with open('events.csv', encoding="utf-8") as table:
    lines = table.readlines()
    rows = read_rows(lines)
    counts = count_types(rows)

with open('summary.csv', "w", encoding="utf-8") as out:
    out.write(to_csv(counts))
