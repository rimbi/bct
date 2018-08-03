def word_to_score(w):
    """
    Given a word <w> returns its Boggle score
    """
    length = len(w)
    if length < 3:
        return 0
    if length in [3, 4]:
        return 1
    if length in [5, 6]:
        return length - 3
    if length == 7:
        return 5
    return 11


def words_to_scores(words):
    """
    Given a list of <words> returns a list of their Boggle scores
    """
    return [word_to_score(word) for word in words]