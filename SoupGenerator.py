import csv
import random
from PIL import Image as pil
import numpy as np

def fixtext(text):
    '''
    Format text
    '''
    return text.replace("'", "").replace("[", "").replace("]", "")

def captext(text):
    '''
    Format and Capitalize text
    '''
    return fixtext(text).capitalize()

def loadlibs(filename):
    lib = []
    path = f'libs/{filename}.csv'
    with open(path, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            lib.extend(row)
    return lib

class Text:
    def number(self, length):
        '''
        length = how many numbers to return
        '''
        return ''.join([str(random.randint(0, 9)) for _ in range(length)])

    def noun(self, length):
        '''
        length = how many nouns to return
        '''
        nouns = loadlibs("nouns")
        return fixtext(" ".join([random.choice(nouns).lower() for _ in range(length)]))

    def adjective(self, length):
        '''
        length = how many adjectives to return
        '''
        adjectives = loadlibs("adjectives")
        return fixtext(" ".join([random.choice(adjectives).lower() for _ in range(length)]))

    def adverb(self, length):
        '''
        length = how many adverbs to return
        '''
        adverbs = loadlibs("adverbs")
        return fixtext(" ".join([random.choice(adverbs).lower() for _ in range(length)]))

    def verb(self, length):
        '''
        length = how many verbs to return
        '''
        verbs = loadlibs("verbs")
        return fixtext(" ".join([random.choice(verbs).lower() for _ in range(length)]))

    def alphabet(self, length):
        '''
        length = how many letters to return
        '''
        alphabets = loadlibs("alphabet")
        return fixtext(" ".join([random.choice(alphabets).lower() for _ in range(length)]))

    def alphanumeric(self, length):
        '''
        length = how many alphanumeric characters to return
        '''
        alphanumeric = loadlibs("alphabet") + list(map(str, range(10)))
        return fixtext("".join([random.choice(alphanumeric) for _ in range(length)]))

    def word(self, length):
        '''
        length = how many words to return
        '''
        adjectives = loadlibs("adjectives")
        adverbs = loadlibs("adverbs")
        nouns = loadlibs("nouns")
        verbs = loadlibs("verbs")
        words = adjectives + adverbs + nouns + verbs
        return captext(" ".join([random.choice(words) for _ in range(length)]) + ".")

class Phrase:
    def noam(self):
        adjectives = loadlibs("adjectives")
        adverbs = loadlibs("adverbs")
        nouns = loadlibs("nouns")
        verbs = loadlibs("verbs")
        val = f'{random.choice(adjectives)} {random.choice(adjectives)} {random.choice(nouns)} {random.choice(verbs)}s {random.choice(adverbs)}. '
        return captext(val)

    def simile(self):
        adjectives = loadlibs("adjectives")
        nouns = loadlibs("nouns")
        val = f'He was as {random.choice(adjectives)} as a {random.choice(nouns)}. '
        return captext(val)

    def cliche(self):
        adverbs = loadlibs("adverbs")
        verbs = loadlibs("verbs")
        val = f'It\'s not rocket science, just {random.choice(adverbs)} {random.choice(verbs)} it. '
        return captext(val)

class SoupImage:
    '''
    dependencies: numpy
    '''
    def __init__(self, width, height, path):
        self.w = width
        self.h = height
        self.path = path
        self.pixels = np.random.randint(255, size=(self.h, self.w), dtype=np.uint8)
        img = pil.fromarray(self.pixels)
        img.save(self.path)

class SoupImageRGB:
    '''
    dependencies: numpy
    '''
    def __init__(self, width, height, path):
        self.w = width
        self.h = height
        self.path = path
        self.pixels = np.random.rand(self.h, self.w, 3) * 255
        img = pil.fromarray(self.pixels.astype('uint8')).convert('RGBA')
        img.save(self.path)

class Audio:
    '''
    dependencies: numpy
    '''
    def wav(self):
        pass

# Example usage
text_gen = Text()
print(text_gen.verb(2))

phrase_gen = Phrase()
print(phrase_gen.noam())
