'''
Soup Generator generates content quickly for use wherever content needs to be.add()

------------------------------
-----example
soupgenerator.Text.noun(2)

-----output
Resistance mastoid

------------------------------

'''
import csv
import random

class Text:

    def number(length):
        '''
        length = how many numbers to return
        '''

        val = ""

        for i in range(length):
            lastnum = val
            val = lastnum + str(random.randint(0,9))

        return str(val)

    def noun(length):
        '''
        length = how many nouns to return
        '''
        length = length
        val = ""
        nouns = __loadlibs("nouns")

        for i in range(length):
            if i > 0:
                lastval = val
                val = lastval + " " + str(random.choice(nouns)).lower()
            else:
                val = str(random.choice(nouns)).lower()
        return __fixtext(val)

    def adjective(length):
        '''
        length = how many adjectives to return
        '''
        length = length
        val = ""
        adjectives = __loadlibs("adjectives")

        for i in range(length):
            if i > 0:
                lastval = val
                val = lastval + " " + str(random.choice(adjectives)).lower()
            else:
                val = str(random.choice(adjectives)).lower()
        return __fixtext(val)

    def adverb(length):
        '''
        length = how many adverbs to return
        '''
        length = length
        val = ""
        adverbs = __loadlibs("adverbs")

        for i in range(length):
            if i > 0:
                lastval = val
                val = lastval + " " + str(random.choice(adverbs)).lower()
            else:
                val = str(random.choice(adverbs)).lower()
        return __fixtext(val)

    def verb(length):
        '''
        length = how many verbs to return
        '''

        length = length
        val = ""
        verbs = __loadlibs("verbs")

        for i in range(length):
            if i > 0:
                lastval = val
                val = lastval + " " + str(random.choice(verbs)).lower()
            else:
                val = str(random.choice(verbs)).lower()
        return __fixtext(val)

    def alphabet(length):
        '''
        length = how many letters to return
        '''

        length = length
        val = ""
        alphabets = __loadlibs("alphabet")

        for i in range(length):
            if i > 0:
                lastval = val
                val = lastval + " " + str(random.choice(alphabets)).lower()
            else:
                val = str(random.choice(alphabets)).lower()
        return __fixtext(val)

    def alphanumeric(length):
        '''
        length = how many letters to return
        '''

        val = ""
        alphanumeric =  __loadlibs("alphabet")

        for i in range(10):
            alphanumeric.append(i)

        for i in range(length):
            if i > 0:
                lastval = val
                val = lastval + str(random.choice(alphanumeric)) 
            else:
                val = str(random.choice(alphanumeric))
            
        return __fixtext(val)

    def word(length):
        '''
        length = how many words to return
        '''
        val = ""
        adjectives = __loadlibs("adjectives")
        adverbs = __loadlibs("adverbs")
        nouns = __loadlibs("nouns")
        verbs = __loadlibs("verbs")

        words = adjectives + adverbs + nouns + verbs

        for i in range(length):
            if i > 0:
                lastval = val
                val = lastval + " " + str(random.choice(words)) 
            else:
                val = str(random.choice(words))
        val = lastval + "."
        return __captext(val)

class Phrase:

    def noam():
        val = ""
        adjectives = __loadlibs("adjectives")
        adverbs = __loadlibs("adverbs")
        nouns = __loadlibs("nouns")
        verbs = __loadlibs("verbs")

        val = f'{random.choice(adjectives)} {random.choice(adjectives)} {random.choice(nouns)} {random.choice(verbs)}s {random.choice(adverbs)}. '

        return __captext(val)

class SoupImage:
    '''
    dependencies: numpy

    width, height = int

    path = str

    ---this will create a png file in the path you specify. that should make it compatible with whatever you need.---

    example: 
    
    soupgenerator.SoupImage(400, 400, 'temp/image.png')
    
    and then you set the source of your tkinter or kivy or pyqt image as the generated image
    '''
    from PIL import Image as pil
    import numpy as np

    def __init__(self, width, height, path):
        self.w = width
        self.h = height
        self.path = path
        self.pixels = self.np.random.randint(255, size=(self.w, self.h), dtype=self.np.uint8)
        img = self.pil.fromarray(self.pixels)
        img.save(self.path)


# stuff
def __fixtext(text):
    ''' Format text '''
    v1 = text.replace("'", "")
    v2 = v1.replace("[", "")
    v3 = v2.replace("]", "")
    return v3

def __captext(text):
    ''' Format and Capitalize text '''
    v = __fixtext(text)
    return v.capitalize()

def __loadlibs(filename):
    lib = []
    path = f'libs/{filename}.csv'
    with open(path, "r") as f:
        r = csv.reader(f)
        for row in r:
            lib.append(row)
    return lib