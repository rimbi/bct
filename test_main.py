from expects import expect, be, equal
from main import word_to_score, words_to_scores, compute_player_scores


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


def test_when_a_player_did_not_find_any_word_its_score_should_be_zero():
    input = {
        'Tom': []
    }
    output = {
        'Tom': 0
    }
    expect(compute_player_scores(input)).to(equal(output))


def test_words_not_unique_to_each_player_should_not_be_counted():
    input = {
        'Tom': ["ammy"],
        'Lucas': ["wine", "house", "ammy"]
    }
    output = {
        'Tom': 0,
        'Lucas': 3,
    }
    expect(compute_player_scores(input)).to(equal(output))
