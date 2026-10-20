def read_rows(lines):
    a = lines[0].split(sep=',')
    r = []
    lines = lines[1:]
    for line in lines:
        line = line.split(sep=',')
        if len(line) != 3:
            continue
        r.append({a[0]:line[0],a[1]:line[1],a[2]:line[2]})
    return r


def count_types(rows):
    counts = {}
    for row in rows:
        kind = row.get("тип")
        if kind is None:
            continue
        counts[kind] = counts.get(kind, 0) + 1
    return counts

def total_minutes(rows, kind):
    r = 0
    for row in rows:
        if row['тип'] == kind:
            r += int(row['минуты'])
    return round(r, 1)

def to_csv(counts):
    r = ['тип,количество']
    for key, value in counts.items():
        v = key + ',' + str(value)
        r.append(v)
    r = '\n'.join(r)
    return r
