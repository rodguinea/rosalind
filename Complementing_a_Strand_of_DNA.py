def reverse_complement(s):
    with open(s, 'r') as f:
        a = f.read()
    dna_string = list(a)
    dna_string.reverse()
    rc = ['A' if nucleobase == 'T' else 'T' if nucleobase == 'A' else 'C' if nucleobase == 'G' else 'G' if nucleobase == 'C' else nucleobase for nucleobase in dna_string]
    return ''.join(rc)


route = 'rosalind_revc.txt'
print(reverse_complement(route))
