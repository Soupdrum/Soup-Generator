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
    
def fixtext(text):
    v1 = text.replace("'", "")
    v2 = v1.replace("[", "")
    v3 = v2.replace("]", "")

    return v3.capitalize()

def loadlibs(filename):
    lib = []
    path = f'libs/{filename}.csv'
    with open(path, "r") as f:
        r = csv.reader(f)
        for row in r:
            lib.append(row)
    return lib


    def alphanumeric(self):
        '''
        length = how many letters to return
        '''

        val = ""
        alphanumeric =  self.loadlists("alphabet")

        for i in range(10):
            alphanumeric.append(i)

        for i in range(self.length):
            if i > 0:
                lastval = val
                val = lastval + str(random.choice(alphanumeric)) 
            else:
                val = str(random.choice(alphanumeric))
            
        return val

    def word():
        return
