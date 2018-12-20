def hamming_distance(s, t):
    strand_s = list(s)
    strand_t = list(t)

    dH = 0

    for i in range(0, len(strand_s)):
        if strand_s[i] != strand_t[i]:
            dH = dH + 1

    return dH
