def check_seq(seq, valid_chars):
    """
    Check that DNA sequence have valid characters.

    Returns False if the check fails
    """
    assert isinstance(valid_chars, list) or isinstance(valid_chars, str), 'Must be either a string or a list of valid characters'

    for nuc in seq:
        if nuc not in valid_chars:
            return False
    
    return True