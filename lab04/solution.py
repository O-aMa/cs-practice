def winner(names: list[str], scores: list[float]) -> str:
    a = scores.index(max(scores))
    return names[a]

def average(scores: list[float]) -> float:
    if scores == []:
        return 0.0
    a = round(sum(scores) / len(scores), 2)
    return a

def ranking(names: list[str], scores: list[float]) -> list[str]:
    r = []
    for i in range(len(names)):
        r.append([names[i], scores[i]])
    r.sort(key=lambda -x[1])
    return [x[0] for x in r]

def above_average(names: list[str], scores: list[float]) -> list[str]:
    r = []
    sr = average(scores)
    a = zip(scores, names)
    for aa in a:
        if aa[0]>sr:
            r.append(aa[1])
    return r
