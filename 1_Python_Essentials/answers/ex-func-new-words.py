def combine_first_letters(sentence):
    """
    takes a sentence (string) and combines the first letters of each word into a new word.
    
    sentence : str
    """
    words = sentence.split()
    new_word=""
    
    for word in words:
        new_word+=word[0]
        
    return new_word

combine_first_letters('this is my example sentence')