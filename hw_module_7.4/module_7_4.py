from dataclasses import replace


class WordsFinder:
    file_names = []

    def __init__(self, *args):
        self.file_names = [*args]

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                text = []
                for line in file:
                    line_ = str(line.lower())
                    line_ = line_.replace(",", "").replace('.', "").replace('=', "").replace('!', "").replace('?', "").replace(';',
                                                                                                                               "").replace(':',
                                                                                                                                           "").replace(' - ', "")
                    line_ = line_.split()
                    text += line_
                all_words[file_name] = text

        return all_words

    def find(self, word):
        finder = {}
        word = word.lower()

        for name, words in self.get_all_words().items():
            try:
                res = words.index(word) + 1
            except:
                res = 0

        finder[name] = res
        return finder

    def count(self, word):
        counter = {}
        word = word.lower()

        for name, words in self.get_all_words().items():
            try:
                res = words.count(word)
            except:
                res = 0

        counter[name] = res
        return counter


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('teXT'))
print(finder2.count('TEXT'))
