import re

# protein dictionary (single letter code and three letter codes)
protein_dic = {"a":"ALA", "b": "ASX", "c":"CYS", "d":"ASP", "e":"GLU", "f":"PHE", "g":"GLY", "h":"HIS", "i":"ILE", "k":"LYS", "l":"LEU", "m":"MET", "n":"ASN", "p":"PRO", "q":"GLN", "r":"ARG", "s":"SER", "t":"THR", "v":"VAL", "w":"TRP", "x":"XAA", "y":"TYR", "z":"GLX", "*":"***"}

#max input user can give
maxInput = 100000000

#function to remove symbols and umbers from sequence
def remove_non_protein_allow_degen(sequence):
    return re.sub(r'[^ABCDEFGHIKLMNPQRSTVWYXZabcdefghiklmnpqrstvwyxz\*]', '', sequence)

# function defined to convert single letter codes to three letter codes
def oneToThree(x):
    x = x.lower()
    for i in x:
        print(protein_dic[i].capitalize(),end="")

#input
protein = input("Paste the raw sequence or one or more FASTA sequences. Input limit is 100,000,000 characters: ")
print()

#function to extract title and sequence from input
def title_and_sequence(protein):
    heading = []
    seq = []

    if protein == "":
        print("Please enter some text.")
    elif len(protein) > maxInput:
            print(f'Sequnce length exceed {maxInput}')
    else:
        # Split by '>'
        parts = re.split(r'\s*>\s*', protein.strip())

        # whether text starts with '>'
        if not protein.strip().startswith('>'):
            heading.append("Untitled")
            cleaned_seq = remove_non_protein_allow_degen(parts[0].strip())
            seq.append(cleaned_seq)
            parts = parts[1:]  
        else:
            if parts[0].strip() == '':
                parts = parts[1:]

        for part in parts:
            part = part.strip()
            match = re.match(r'([^\d\W]\w*(?:[\s_]+\w+)*)\s+(.*)', part)
            if match:
                head, sequence = match.groups()
                heading.append(head.strip())
                cleaned_seq = remove_non_protein_allow_degen(sequence.strip())
                seq.append(cleaned_seq)
            else:
                heading.append("Untitled")
                cleaned_seq = remove_non_protein_allow_degen(part.strip())
                seq.append(cleaned_seq)

    return heading, seq

heading , seq = title_and_sequence(protein)

#function to write the result
def write(heading, seq):
    # matiching the title and sequence
    new_protein = list(zip(heading, seq))
    for title, residue in new_protein:
        len_residue = len(residue)
        starting = residue[0:11]
        print("OnetoThree\n")
        print(f"> result for {len_residue} sequence '{title}' starting '{starting}'")
        oneToThree(residue)
        print("\n")

write(heading, seq)