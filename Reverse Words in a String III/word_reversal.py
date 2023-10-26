def rev_string(s):
    temp_string = s.split()
    rev_words = [word[::-1] for word in temp_string ]
    result = ' '.join(rev_words)
    return result