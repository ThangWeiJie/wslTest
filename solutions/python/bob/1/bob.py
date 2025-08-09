def response(hey_bob):
    proper_sentence = hey_bob.strip()

    if(proper_sentence.isupper() and proper_sentence.endswith('?')):
        return "Calm down, I know what I'm doing!"
    elif(proper_sentence.isupper()):
        return "Whoa, chill out!"
    elif(proper_sentence.endswith('?')):
        return "Sure."
    elif(proper_sentence == ''):
        return "Fine. Be that way!"
    else:
        return "Whatever."
