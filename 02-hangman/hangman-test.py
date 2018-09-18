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

	def test_counts_failures_when_letter_is_incorrectly_guessed(self):
		game = Hangman('a')
		last_incorrect_guesses = game.get_guesses()

		game.guess_letter('b')

		self.assertEqual(game.get_guesses(), last_incorrect_guesses + 1)

	def test_does_not_count_failures_when_letter_is_correctly_guessed(self):
		game = Hangman('a')
		last_incorrect_guesses = game.get_guesses()

		game.guess_letter('a')

		self.assertEqual(game.get_guesses(), last_incorrect_guesses)

	def test_game_is_running_after_startup(self):
		game = Hangman('a')

		self.assertEqual(game.get_status(), 'Running')

	def test_game_is_lost_when_guessed_incorrectly_for_11_times(self):
		game = Hangman('a')

		for _ in range(11):
			game.guess_letter('b')

		self.assertEqual(game.get_status(), 'Lost')

	def test_game_is_NOT_lost_when_guessed_incorrectly_for_10_times(self):
		game = Hangman('a')

		for _ in range(10):
			game.guess_letter('b')

		self.assertEqual(game.get_status(), 'Running')
	
	def test_game_is_won_when_all_guessed_correctly(self):
		game = Hangman('abbc')

		game.guess_letter('a')
		game.guess_letter('b')
		game.guess_letter('c')

		self.assertEqual(game.get_status(), 'Won')



if __name__ == '__main__':
	unittest.main(verbosity=2)
