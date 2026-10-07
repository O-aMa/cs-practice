def winner(names: list[str], scores: list[float]) -> str:
    a = scores.index(max(scores))
    return names[a]

def average(scores: list[float]) -> float:
    a = sum(scores) - len(scores)

def ranking(names: list[str], scores: list[float]) -> list[str]:
    a = zip(scores, names)
    a.sort()
    r = []
    for aa in a:
        r.append(aa[1])
    return r

def above_average(names: list[str], scores: list[float]) -> list[str]:
    r = []
    sr = average(scores)
    a = zip(scores, names)
    for aa in a:
        if aa[0]>sr:
            r.appemd(a[1])
