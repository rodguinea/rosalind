from __future__ import division
import numpy as np


def cg_content(s):
    with open(s, 'r') as f:
        a = f.read()
    letters = list()
    index = list()
    repo = list()
    dna_string = a.split("\n")

    for word in dna_string:
        x = list(word)
        letters.append(x)

    for i in range(0, len(letters)):
        if letters[i][0] == ">":
            index.append(i)

    t = len(index) - 1
    for i in range(0, t + 1):
        aux = list()
        if i == t:
            b = range(index[i] + 1, len(letters))
        else:
            b = range(index[i] + 1, index[i + 1])
        a = np.array(letters)
        lst = list(a[b])
        for element in lst:
            aux.extend(element)

        repo.append([dna_string[index[i]], sum(i == 'C' or i == 'G' for i in aux) / len(aux) * 100])

    aux = max(repo, key=lambda x: x[1])

    return "%s\n%s" % (aux[0].replace(">", ""), aux[1])


route = 'rosalind_gc.txt'
print(cg_content(route))
