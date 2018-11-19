def population(n, k):
    time_lapse = [i for i in range(1, n + 1)]
    rate = k
    couples = 0
    babies = 1
    parents = 0

    for t in time_lapse:
        total = parents + couples + babies
        parents = parents + couples
        couples = babies
        babies = parents * rate

    return total
