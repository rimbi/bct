#!/usr/bin/env python

"""game.py: A mini Boggle game implementation."""
from score import GameScore


class Game(object):
    """
    Represents a Boggle game
    """

    def __init__(self, board, dictionary, ui):
        self.dictionary = dictionary
        self.board = board
        self.ui = ui
        self.solutions = {}

    def submit_solution(self, player_name, words):
        """
        Adds <words> found by <player_name> during the game
        """
        words = [word for word in words
                 if word in self.dictionary and self.board.contains(word)]
        self.solutions[player_name] = words

    def scores(self):
        """
        Given the players submitted their solutions computes the scores
        """
        return GameScore.compute_player_scores(self.solutions)

    def play(self):
        """
        Executes main game logic
        """
        number_of_players = self.ui.get_number_of_players()
        for i in range(number_of_players):
            name = self.ui.get_player_name(i)
            words = self.ui.get_words_found_by_player(name)
            self.submit_solution(name, words)
