def dna_to_rna(s):
    with open(s, 'r') as f:
        a = f.read()
    dna_string = list(a)
    rna_string = ['U' if nucleobase == 'T' else nucleobase for nucleobase in dna_string]
    return ''.join(rna_string)


route = 'rosalind_rna.txt'
print(dna_to_rna(route))
