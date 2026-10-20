from tablestats import *
with open(r'C:\Users\Roman\Desktop\cs-practice\lab05\events.csv', encoding="utf-8") as table:
    lines = table.readlines()
    rows = read_rows(lines)
    counts = count_types(rows)

with open(r'C:\Users\Roman\Desktop\cs-practice\lab05\summary.csv', "w", encoding="utf-8") as out:
    out.write(to_csv(counts))
