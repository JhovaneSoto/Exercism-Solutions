def response(hey_bob):
    
    hey_bob=hey_bob.strip()
    

    if hey_bob.upper()==hey_bob and hey_bob.endswith("?") and any(c.isalpha() for c in hey_bob):
        return "Calm down, I know what I'm doing!"

    if hey_bob.endswith("?"):
        return "Sure."

    if hey_bob.upper()==hey_bob and any(c.isalpha() for c in hey_bob):
        return "Whoa, chill out!"

    if hey_bob.strip()=="":
        return "Fine. Be that way!"
    
    return "Whatever."