def read_rows(lines):
    rows = []
    header = None
    for line in lines:
        line = line.strip()
        if not line:
            continue
        fields = [f.strip() for f in line.split(",")]
        if header is None:
            header = fields
            continue
        if len(fields) != len(header):
            continue
        rows.append(dict(zip(header, fields)))
    return rows



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
    lines = ["тип,количество"]
    for kind in sorted(counts):
        lines.append(f"{kind},{counts[kind]}")
    return "\n".join(lines) + "\n"
