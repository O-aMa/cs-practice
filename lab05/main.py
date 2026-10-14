from tablestats import *
with open('events.csv', encoding="utf-8") as table:
    rows = read_rows(table)
    counts = count_types(rows)

with open("summary.csv", "w", encoding="utf-8") as out:
    out.write(to_csv(counts))
