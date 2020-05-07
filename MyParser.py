#!/usr/bin/env python

"""
Original author: Paul Boddie <paul@boddie.org.uk>

To the extent possible under law, the person who associated CC0 with this work
has waived all copyright and related or neighboring rights to this work.

See: http://creativecommons.org/publicdomain/zero/1.0/
"""

import sgmllib

class MyParser(sgmllib.SGMLParser):
    "A simple parser class."

    def parse(self, s):
        "Parse the given string 's'."
        self.feed(s)
        self.close()

    def __init__(self, verbose=0):
        "Initialise an object, passing 'verbose' to the superclass."

        sgmllib.SGMLParser.__init__(self, verbose)
        self.hyperlinks = []

    def start_a(self, attributes):
        "Process a hyperlink and its 'attributes'."

        for name, value in attributes:
            if name == "href":
                self.hyperlinks.append(value)

    def get_hyperlinks(self):
        "Return the list of hyperlinks."

        return self.hyperlinks

import urllib, sgmllib

# Get something to work with.
f = urllib.urlopen("http://www.python.org")
s = f.read()

# Try and process the page.
# The class should have been defined first, remember.
myparser = MyParser()
myparser.parse(s)

# Get the hyperlinks.
print myparser.get_hyperlinks()
