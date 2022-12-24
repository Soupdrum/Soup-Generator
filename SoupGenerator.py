#pylint:disable=E0211
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
        nouns = loadlibs("nouns")

        for i in range(length):
            if i > 0:
                lastval = val
                val = lastval + " " + str(random.choice(nouns)).lower()
            else:
                val = str(random.choice(nouns)).lower()
        return fixtext(val)

    def adjective(length):
        '''
        length = how many adjectives to return
        '''
        length = length
        val = ""
        adjectives = loadlibs("adjectives")

        for i in range(length):
            if i > 0:
                lastval = val
                val = lastval + " " + str(random.choice(adjectives)).lower()
            else:
                val = str(random.choice(adjectives)).lower()
        return fixtext(val)

    def adverb(length):
        '''
        length = how many adverbs to return
        '''
        length = length
        val = ""
        adverbs = loadlibs("adverbs")

        for i in range(length):
            if i > 0:
                lastval = val
                val = lastval + " " + str(random.choice(adverbs)).lower()
            else:
                val = str(random.choice(adverbs)).lower()
        return fixtext(val)

    def verb(length):
        '''
        length = how many verbs to return
        '''

        length = length
        val = ""
        verbs = loadlibs("verbs")

        for i in range(length):
            if i > 0:
                lastval = val
                val = lastval + " " + str(random.choice(verbs)).lower()
            else:
                val = str(random.choice(verbs)).lower()
        return fixtext(val)

    def alphabet(length):
        '''
        length = how many letters to return
        '''

        length = length
        val = ""
        alphabets = loadlibs("alphabet")

        for i in range(length):
            if i > 0:
                lastval = val
                val = lastval + " " + str(random.choice(alphabets)).lower()
            else:
                val = str(random.choice(alphabets)).lower()
        return fixtext(val)

    def alphanumeric(length):
        '''
        length = how many letters to return
        '''

        val = ""
        alphanumeric =  loadlibs("alphabet")

        for i in range(10):
            alphanumeric.append(i)

        for i in range(length):
            if i > 0:
                lastval = val
                val = lastval + str(random.choice(alphanumeric)) 
            else:
                val = str(random.choice(alphanumeric))
            
        return fixtext(val)

    def word(length):
        '''
        length = how many words to return
        '''
        val = ""
        adjectives = loadlibs("adjectives")
        adverbs = loadlibs("adverbs")
        nouns = loadlibs("nouns")
        verbs = loadlibs("verbs")

        words = adjectives + adverbs + nouns + verbs

        for i in range(length):
            if i > 0:
                lastval = val
                val = lastval + " " + str(random.choice(words)) 
            else:
                val = str(random.choice(words))
        val = lastval + "."
        return captext(val)
        
class Text2:
    def constructor(self):
        self.nouns = loadlibs("nouns")
        self.adjectives = loadlibs("adjectives")
        self.adverbs = loadlibs("adverbs")
        self.verbs = loadlibs("verbs")
        self.alphabets = loadlibs("alphabet")
        self.alphanumeric = self.alphabets + list(range(10))
        self.words = self.adjectives + self.adverbs + self.nouns + self.verbs
        
    def number(length):
        '''
        length = how many numbers to return
        '''
        return str(''.join([str(random.randint(0,9)) for _ in range(length)]))

    def noun(length):
        '''
        length = how many nouns to return
        '''
        return fixtext(" ".join([random.choice(self.nouns).lower() for _ in range(length)]))

    def adjective(length):
        '''
        length = how many adjectives to return
        '''
        return fixtext(" ".join([random.choice(self.adjectives).lower() for _ in range(length)]))

    def adverb(length):
        '''
        length = how many adverbs to return
        '''
        return fixtext(" ".join([random.choice(self.adverbs).lower() for _ in range(length)]))

    def verb(length):
        '''
        length = how many verbs to return
        '''
        return fixtext(" ".join([random.choice(self.verbs).lower() for _ in range(length)]))

    def alphabet(length):
        '''
        length = how many letters to return
        '''
        return fixtext(" ".join([random.choice(self.alphabets).lower() for _ in range(length)]))

    def alphanumeric(length):
        '''
        length = how many letters to return
        '''
        return fixtext("".join([str(random.choice(self.alphanumeric)) for _ in range(length)]))

    def word(length):
        '''
        length = how many words to return
        '''
        return captext(" ".join([random.choice(self.words) for _ in range(length)]) + ".")
        
print(Text2.verb(1))

class Phrase:

    def noam():

        val = ""
        adjectives = loadlibs("adjectives")
        adverbs = loadlibs("adverbs")
        nouns = loadlibs("nouns")
        verbs = loadlibs("verbs")

        val = f'{random.choice(adjectives)} {random.choice(adjectives)} {random.choice(nouns)} {random.choice(verbs)}s {random.choice(adverbs)}. '

        return captext(val)
        
    def simile():
    	val = ""
    	adjectives = loadlibs("adjectives")
    	nouns = loadlibs("nouns")
    	val = f'He was as {random.choice(adjectives)} as a {random.choice(nouns)}. '
    	return captext(val)
    	
    def cliche():

        val = ""
        adverbs = loadlibs("adverbs")
        verbs = loadlibs("verbs")
        val = f'It\'s not rocket science, just {random.choice(adverbs)} {random.choice(verbs)} it. '

        return captext(val)
    	

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
        self.pixels = self.np.random.randint(255, size=(self.h, self.w), dtype=self.np.uint8)
        img = self.pil.fromarray(self.pixels)
        img.save(self.path)
        
class SoupImageRGB:
	from PIL import Image as pil
	import numpy as np
	
	def __init__(self, width, height, path):
		self.w = width
		self.h = height
		self.path = path
		self.pixels = self.np.random.rand(self.h, self.w, 3) * 255
		img = self.pil.fromarray(self.pixels.astype('uint8')).convert('RGBA')
		img.save(self.path)

class Audio:
    '''
    depencencies: numpy
    '''
    import numpy as np


    def wav(self):
        pass

def fixtext(text):
    '''
    Format text
    '''
    v1 = text.replace("'", "")
    v2 = v1.replace("[", "")
    v3 = v2.replace("]", "")

    return v3

def captext(text):
    '''
    Format and Capitalize text
    '''
    v = fixtext(text)

    return v.capitalize()

def loadlibs(filename):
    lib = []
    path = f'libs/{filename}.csv'
    with open(path, "r") as f:
        r = csv.reader(f)
        for row in r:
            lib.append(row)
    return lib
    