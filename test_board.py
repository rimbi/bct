#!/usr/bin/env python

"""test_board.py: Tests for Board class."""

from expects import expect, be, equal
from board import Board, Cell


def test_board_should_say_no_when_the_word_is_not_in_board():
    # given
    board = Board(['ADHG', 'PDFF', 'EKJU', 'FTGT'])
    # when
    res = board.contains('CAT')
    # then
    expect(res).to(be(False))

#
# def test_board_should_recognize_verticle_words():
#     # given
#     board = Board(['CDHG', 'ADFF', 'TKJU', 'FTGT'])
#     # when
#     res = board.contains('CAT')
#     # then
#     expect(res).to(be(True))


def test_given_a_char_board_should_return_corresponding_cells():
    # given
    board = Board(['CDHG', 'ADFF', 'TKJU', 'FTGT'])
    # when
    res = board.get_cells_of_char('F')
    # then
    expect(list(res)).to(equal([Cell('F', 1, 2), Cell('F', 1, 3), Cell('F', 3, 0)]))


def test_given_a_corner_cell_it_should_return_coordinates_of_correct_neighbours():
    # given
    cell = Cell('C', 0, 0)
    # when
    res = cell.get_coordinates_of_neighbours()
    # then
    expect(set(res)).to(equal(set([(1, 0), (1, 1), (0, 1)])))


def test_given_a_edge_cell_it_should_return_coordinates_of_correct_neighbours():
    # given
    cell = Cell('C', 1, 0)
    # when
    res = cell.get_coordinates_of_neighbours()
    # then
    expect(set(res)).to(equal(set([(0, 0), (0, 1), (1, 1), (2, 0), (2, 1)])))


def test_cells_with_same_values_should_be_equal():
    # given
    cell1 = Cell('C', 1, 0)
    cell2 = Cell('C', 1, 0)
    # when
    res = cell1 == cell2
    # then
    expect(res).to(be(True))


def test_given_a_corner_cell_board_should_return_neighbour_cells():
    # given
    board = Board(['CDHG', 'ADFF', 'TKJU', 'FTGT'])
    cell = Cell('C', 0, 0)
    # when
    res = board.get_neighbour_cells(cell)
    # then
    expect(set(res)).to(equal(set([Cell('A', 1, 0), Cell('D', 1, 1), Cell('D', 0, 1)])))


def test_board_should_verify_single_char_words():
    # given
    board = Board(['CDHG', 'ADFF', 'TKJU', 'FTGT'], dictionary=['F', 'DOG'])
    # when
    res = board.contains('F')
    # then
    expect(res).to(be(True))


def test_board_should_verify_vertical_two_chars_words():
    # given
    board = Board(['CDHG', 'ADFF', 'TKJU', 'FTGT'], dictionary=['FU', 'DOG'])
    # when
    res = board.contains('FU')
    # then
    expect(res).to(be(True))


def test_board_should_verify_horizontal_two_chars_words():
    # given
    board = Board(['CDHG', 'ADFF', 'TKJU', 'FTGT'], dictionary=['AD', 'DOG'])
    # when
    res = board.contains('AD')
    # then
    expect(res).to(be(True))


def test_board_should_verify_diagonal_two_chars_words():
    # given
    board = Board(['CDHG', 'ADFF', 'TKJU', 'FTGT'], dictionary=['AT', 'DOG'])
    # when
    res = board.contains('AT')
    # then
    expect(res).to(be(True))


def test_board_should_verify_vertical_plus_horizontal_words():
    # given
    board = Board(['CDHG', 'ADFF', 'TKJU', 'FSET'], dictionary=['CAT', 'FUTES'])
    # when
    res = board.contains('FUTES')
    # then
    expect(res).to(be(True))


def test_board_should_not_verify_words_not_in_the_dictionary():
    # given
    board = Board(['CATG', 'ADFF', 'TKJU', 'FSET'], dictionary=['CAT', 'DOG'])
    # when
    res = board.contains('AD')
    # then
    expect(res).to(be(False))
