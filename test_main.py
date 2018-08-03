from expects import expect, be, equal
from main import word_to_score
from main import words_to_scores


def test_word_to_score():
    words_dict = dict((
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
    ))
    for w, s in words_dict.iteritems():
        expect(word_to_score(w)).to(be(s))


def test_words_to_scores():
    words = (
        "catty",
        "wampus",
        "am",
        "bumfuzzle",
        "gardyloo",
        "taradiddle",
        "loo",
        "snickersnee",
        "widdershins",
        "teabag",
        "collywobbles",
        "gubbins"
    )
    scores = [2, 3, 0, 11, 11, 11, 1, 11, 11, 3, 11, 5]
    expect(words_to_scores(words)).to(equal(scores))
