
# one-letter codes for amino acids
valid_aas = 'ARNDCQEGHILKMFPSTWYV'
ambigious_aas = 'XJZB'

# and in case of aligned sequences
valid_aas_aln = valid_aas + '*-'

# one letter code to name
aa2name = {
    'A': 'Alanine', 
    'R': 'Arginine', 
    'N': 'Asparagine',
    'D': 'Aspartic Acid', 
    'C': 'Cysteine',
    'Q': 'Glutamine', 
    'E': 'Glutamic Acid', 
    'G': 'Glycine', 
    'H': 'Histidine',
    'I': 'Isoleucine', 
    'L': 'Leucine',
    'K': 'Lysine',
    'M': 'Methionine', 
    'F': 'Phenylalanine',
    'P': 'Proline', 
    'S': 'Serine',
    'T': 'Threonine',
    'W': 'Tryptophan',
    'Y': 'Tyrosine',
    'V': 'Valine',
    'B': 'Aspargine or aspartic acid',
    'Z': 'Glutamine or glutamic acid',
    'J': 'Leucine or isoleucine',
    'X': 'Unknown',
    '-': 'Gap',
    '*': 'Termination'
}

# single letter to three letter code for amino acids
aa2three = {
    'A': 'Ala',
    'R': 'Arg',
    'N': 'Asn',
    'D': 'Asp',
    'C': 'Cys',
    'Q': 'Gln',
    'E': 'Glu',
    'G': 'Gly',
    'H': 'His',
    'I': 'Ile',
    'L': 'Leu',
    'K': 'Lys',
    'M': 'Met',
    'F': 'Phe',
    'P': 'Pro',
    'S': 'Ser',
    'T': 'Thr',
    'W': 'Trp',
    'Y': 'Tyr',
    'V': 'Val',
    'B': 'Asx',
    'Z': 'Glx',
    'J': 'Xle',
    'X': 'Xaa'
}

# amino acid to codons
aa2codons = {
    'A': ['GCU', 'GCC', 'GCA','GCG'],
    'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'N': ['AAU', 'AAC'],
    'D': ['GAU', 'GAC'],
    'C': ['UGU', 'UGC'],
    'Q': ['CAA', 'CAG'],
    'E': ['cid', 'GAA', 'GAG'],
    'G': ['GGU', 'GGC', 'GGA', 'GGG'],
    'H': ['CAU', 'CAC'],
    'I': ['AUU', 'AUC', 'AUA'],
    'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
    'K': ['AAA', 'AAG'],
    'M': ['AUG'],
    'F': ['UUU UUC'],
    'P': ['CCU', 'CCC', 'CCA', 'CCG'],
    'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
    'T': ['ACU', 'ACC', 'ACA', 'ACG'],
    'W': ['UGG'],
    'Y': ['UAU', 'UAC'],
    'V': ['GUU', 'GUC', 'GUA', 'GUG'],
    'B': ['AAU', 'AAC', 'GAU', 'GAC'],
    'Z': ['AAU', 'AAC', 'GAU', 'GAC'],
    'J': ['AUU', 'AUC', 'AUA', 'UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
}