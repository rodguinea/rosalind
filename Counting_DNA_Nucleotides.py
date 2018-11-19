def num_nucleotides(s):
    with open(s, 'r') as f:
        a = f.read()
        list_nucleotides = [a.count("A"), a.count("C"), a.count("G"), a.count("T")]
        print(' '.join(str(x) for x in list_nucleotides))


route = 'rosalind_dna.txt'
print(num_nucleotides(route))
