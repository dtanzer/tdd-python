class Hangman:
	def __init__(self,word):
		self._word=word
		self._letter=str()

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
		

if __name__=="__main__":
	A=Hangman()
