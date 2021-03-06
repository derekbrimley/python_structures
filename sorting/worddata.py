#!/usr/bin/env python3

class WordData(object):
    '''Data about a single word'''

    def __init__(self, book, word, count):
        '''Constructor'''
        self.book = book
        self.word = word
        self.count = count
        self.percent = None

    def __str__(self):
        # 1 Nephi,the,2141,8.1
        return '{},{},{},{}'.format(
            self.book, self.word, self.count, self.percent)

    def set_percent(self, total):
        self.percent = round(100 * float(self.count)/float(total), 1)
