from expects import expect, be


def test_word_to_score():
    words_dict = dict(
        ("catty", 2),
        ("wampus", 3),
        ("am", 0),
        ("bumfuzzle", 11),
        ("gardyloo", 11),
        ("taradiddle", 11),
        ("loo", 1),
        ("snickersnee", 11),
        ("widdershins", 11),
        ("teabag", 3),
        ("collywobbles", 11),
        ("gubbins", 5)
    )
    for w, s in words_dict.iteritems():
        expect(words_to_score(w)).to(be(s))
