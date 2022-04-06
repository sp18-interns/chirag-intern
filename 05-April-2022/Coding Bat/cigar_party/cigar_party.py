def cigar_party(cigars, is_weekend):
    if 40 <= cigars <= 60:
        return True
    elif is_weekend:
        return cigars >= 40
    else:
        return False
