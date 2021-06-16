# Create your Phrase class logic here.
class Phrase:
    def __init__(self, in_phrase):
        self.phrase = in_phrase.lower()
        self.phrase_list = []
        self.phrase_display = []
        for char in self.phrase:
            self.phrase_list.append(char)
            if char == " ":
                self.phrase_display.append(" ")
            else:
                self.phrase_display.append("_")

    def display(self):
        #  prints out the phrase to the console with _ or letter
        print(" ".join(self.phrase_display))

    def check_letter(self, in_letter):
        #  checks to see if letter selected matches a letter in the phrase
        if in_letter in self.phrase_list:
            for index, char in enumerate(self.phrase_list):
                if char == in_letter:
                    self.phrase_display[index] = in_letter
            return True
        else:
            return False

    def check_complete(self):
        #  checks to see if the whole phrase has been guessed
        return "_" not in self.phrase_display


phrase = Phrase("hello wo")
phrase.display()