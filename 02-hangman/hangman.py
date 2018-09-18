class Hangman:
	def __init__(self,word):
		self._word=word
		self._letter=str()
		self.incorrect_guesses = 0

	def render_hint(self):
		output = str()

		for i in self._word:
			if i in self._letter:
				output+= i
			else:
				output+= '.'

		return output

	def guess_letter(self, letter):
		self._letter+=letter
		self.incorrect_guesses+=1
		

if __name__=="__main__":
	A=Hangman()
