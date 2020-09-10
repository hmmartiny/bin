from protein import codon2aa

def check_seq(seq, valid_chars):
    """
    Check that a sequence have valid characters.

    Returns False if the check fails
    """
    assert isinstance(valid_chars, list) or isinstance(valid_chars, str), 'Must be either a string or a list of valid characters'

    for s in seq:
        if s not in valid_chars:
            return False
    
    return True

def translate(seq, d):
    """
    Translate a sequence by using the dictionary d as the lookup table.

    Returns the translated amino acid sequence.
    """

    translated = []
    N = len(d)

    if not check_seq(seq, list(d.keys())):
        raise KeyError('Not a valid sequence')

    for i in range(0, N, 3):
        s = seq[i:i+3]
        translated.append(d[s])
    
    return translated

def transcribe(seq):
    """
    Turn a DNA sequence into a RNA sequence like in transcription.
    """

    seq = seq.replace('T', 'U')

    return seq