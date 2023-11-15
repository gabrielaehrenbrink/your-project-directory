class GrammarStats:
    def __init__(self):
        self.passed_count = 0
        self.total_count = 0

    def check(self, text):
        self.text = text
        punctuation = '.!?'
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        if self.text[0].isupper() and self.text[-1] in punctuation:
            self.passed_count += 1
            self.total_count += 1
            return True
        else:
            self.total_count += 1
            return False

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        if self.total_count == 0:
            return 0
        percentage = (self.passed_count / self.total_count) * 100
        return int(percentage)