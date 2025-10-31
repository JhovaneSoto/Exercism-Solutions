def find_anagrams(word, candidates):
    return [palabra for palabra in candidates if is_anagram(word,palabra)]

def is_anagram(word_a,word_b):
    if word_a.upper()==word_b.upper():
        return False
    word_a=sorted(list(word_a.upper()))
    word_b=sorted(list(word_b.upper()))
    
    return word_a==word_b
