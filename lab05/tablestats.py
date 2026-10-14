def read_rows(lines):
    a = lines[0].split(sep=',')
    r = []
    lines = lines[1:]
    for line in lines:
        line = line.split(sep=',')
        if line.count() != 3:
            continue
        r.append(dict(a[0]=line[0],a[1]=line[1],a[2]=line[2]))
    return r


def count_types(rows):
    z = 0
    o = 0
    v = 0
    p = 0
    for row in rows:
        if row['тип'] == 'запуск':
            z += 1
        elif row['тип'] == 'ошибка':
            o += 1
        elif row['тип'] == 'проверка':
            p += 1
        elif row['тип'] == 'выгрузка':
            v += 1
    counts = {'запуск': z, 'ошибка': o, 'проверка': p, 'выгрузка': v}
    return counts

def total_minutes(rows, kind):
    r = 0
    for row in rows:
        if row['тип'] == kind:
            r += row['минуты']
    return round(r, 1)

def to_csv(counts):
    r = ['тип, количество']
    for key, value in counts:
        v = key + str(value)
        r.apeend(v)
    r = '\n'.join(r)
    return r
