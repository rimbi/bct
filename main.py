#!/usr/bin/env python

"""main.py: A mini Boggle game implementation."""
import string

from board import Board
from game import Game

MIN_NUMBER_OF_PLAYERS = 2


class ConsoleUI(object):

    def get_number_of_players(self):
        """
        Reads number of players in the game from the console and returns it.
        """
        number_of_players = 0
        while number_of_players < MIN_NUMBER_OF_PLAYERS:
            try:
                number_of_players = int(raw_input('Number of players: '))
                if number_of_players < MIN_NUMBER_OF_PLAYERS:
                    print('The number of players must be at least {}'.format(
                        MIN_NUMBER_OF_PLAYERS))
            except ValueError:
                print('Please enter a valid number')
        return number_of_players

    def get_player_name(self, i):
        """
        Reads <i>th player name from the console and returns it.
        It can not be empty.
        """
        name = ''
        while not name:
            name = raw_input('Name of the player {}: '.format(i+1))
            if not name:
                print('Please enter a valid name')
        return name

    @staticmethod
    def is_ascii(str):
        """
        Checks if string <str> is composed of all ASCII chars
        """
        return all(c in string.letters for c in str)

    def get_words_found_by_player(self, player_name):
        """
        Reads the words found by <player_name> from console and returns them as list
        """
        words = ''
        while not words:
            words = raw_input('Words found by player {}: '.format(player_name))
            if not words:
                print('Please enter some words')
            if not self.is_ascii(''.join(words.split(' '))):
                print('Please enter ASCII words')
                words = ''

        return [word for word in words.upper().split(' ') if word]


def get_dictionary_from_user():
    """
    Returns the list of dictionary items from console input
    """
    dictionary = ''
    while not dictionary:
        dictionary = raw_input('Enter the valid dictionary: ')
        if not dictionary:
            print('Please enter some dictionary')
        if not is_ascii(''.join(dictionary.split(' '))):
            print('Please enter ASCII dictionary')
            dictionary = ''

    return [word for word in dictionary.upper().split(' ') if word]


def get_dictionary_from_file(file_path):
    """
    Returns the list of dictionary items in <file_path>
    """
    with open(file_path) as fp:
        return [line.strip().upper() for line in fp]


def print_board(board):
    for row in board:
        print ' '.join(row)


def generate_board_config():
    """
    Generates a random board config as a list of 4 strings of length 4.
    Example: ['ASDE', 'FEHZ', 'DVHJ', 'JZUK']
    """
    import random
    import string
    str = ''.join(random.choice(string.uppercase) for _ in range(16))
    return [str[:4], str[4:8], str[8:12], str[12:]]


def main():
    config = generate_board_config()
    print config
    print_board(config)
    board = Board(config)
    # dictionary = get_dictionary_from_user()
    dictionary = get_dictionary_from_file('./wordlist-english.txt')
    ui = ConsoleUI()
    game = Game(board, dictionary, ui)
    game.play()
    print 'Scores'
    print '------'
    for player, score in game.scores().items():
        print '{} : {}'.format(player, score)


if __name__ == '__main__':
    main()
