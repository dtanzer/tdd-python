import unittest
from hangman import Hangman

class TestHangman(unittest.TestCase):
	
	def test_returns_1_dot_if_1_letter_after_game_start(self):
		game=Hangman("a")

		hint = game.render_hint()

		self.assertEqual(hint,".")

	def test_returns_2_dots_if_2_letters_after_game_start(self):
		game=Hangman("ab")

		hint = game.render_hint()

		self.assertEqual(hint,"..")

	@unittest.skip('think about what happens if space after string')
	def test_handle_spaces(self):
		pass

	def test_return_aDot_if_a_is_correctly_guessed_if_word_is_ab(self):
		game = Hangman('ab')
		game.guess_letter('a')

		hint = game.render_hint()

		self.assertEqual(hint,'a.')

	def test_return_ab_if_ab_is_correctly_guessed(self):
		game = Hangman('ab')
		game.guess_letter('a')
		game.guess_letter('b')

		hint = game.render_hint()

		self.assertEqual(hint,'ab')

	def test_return_a_if_a_is_correctly_guessed(self):
		game = Hangman('a')
		game.guess_letter('a')

		hint = game.render_hint()

		self.assertEqual(hint,'a')

if __name__ == '__main__':
	unittest.main(verbosity=2)
