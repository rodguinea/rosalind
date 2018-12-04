def dna_to_rna(s):
    with open(s, 'r') as f:
        content = f.readlines()
    i = 1
    new_content = []
    for line in content:
        if i % 2 == 0:
            new_content.append(line)
        i = i + 1
    return new_content


s = 'rosalind_ini5.txt'
text = dna_to_rna(s)

for n in range(0, len(text)):
    print(text[n], end='')
