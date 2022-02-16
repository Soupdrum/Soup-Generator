'''
Soup Generator generates content quickly for use wherever content needs to be.add()

------------------------------
-----example
soupgenerator.Text.number(4)

-----output
8432

------------------------------



'''
import json
import random

length = 0


class Text:

    def number(length):
        '''
        length = how many numbers to return
        '''
        num = ""

        for i in range(length):
            lastnum = num
            num = lastnum + str(random.randint(0,9))

        return str(num)

    def alphabet():
        return

    def alphanumeric():
        vals = "HI"
        return

    def words():
        return

    def paragraphs():
        return
