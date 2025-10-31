def is_pangram(sentence):
    return True if len(set([c.upper() for c in sentence if c.isalpha()]))==26 else False
