def winner(names: list[str], scores: list[float]) -> str:
    a = scores.index(max(scores))
    return names[a]

def average(scores: list[float]) -> float:
    if scores == []:
        pass
    else:
        a = round(sum(scores) / len(scores), 2)
        return a

def ranking(names: list[str], scores: list[float]) -> list[str]:
    a = zip(names,scores)
    a = sorted(a, key = lambda x: x, Reverse=True)
    r = []
    for aa in ar:
        r.append(aa[1])
    return r

def above_average(names: list[str], scores: list[float]) -> list[str]:
    r = []
    sr = average(scores)
    a = zip(scores, names)
    for aa in a:
        if aa[0]>sr:
            r.append(aa[1])
    return r
