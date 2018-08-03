#!/usr/bin/env python

"""score.py: A package to calculate Boggle game scores."""


class GameScore(object):

    def __init__(self):
        pass

    @staticmethod
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

    @staticmethod
    def words_to_scores(words):
        """
        Given a list of <words> returns a list of their Boggle scores
        """
        return [GameScore.word_to_score(word) for word in words]

    @staticmethod
    def compute_player_scores(players_and_words):
        """
        Given the final board situation as <players_and_words> returns players and their scores as dict
        """
        def unique_words_of_player(player):
            o = [set(players_and_words[p])
                 for p in players_and_words if p != player]
            other_words = reduce(lambda x, y: x | y, o, set())
            unique_words = set(players_and_words[player]) - other_words
            return unique_words

        return {player: sum(GameScore.words_to_scores(unique_words_of_player(player)))
                for player in players_and_words}
