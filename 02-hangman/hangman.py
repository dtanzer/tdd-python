class Hangman:
    def __init__(self,word):
        self._word=word
        self._letter=str()
        self._incorrect_guesses = 0
        self._status = 'Running'

    def get_guesses(self):
        return self._incorrect_guesses

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
        if not letter in self._word:
            self._incorrect_guesses+=1

        if self._incorrect_guesses >= 11:
            self._status = 'Lost'
        
        if '.' not in self.render_hint():
            self._status = 'Won'

    def get_status(self):
        return self._status

if __name__=="__main__":
    A=Hangman('The')
