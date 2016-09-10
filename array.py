#!/usr/bin/env python3

import os
import sys
import argparse


class Array(object):
    '''
    An array implementation that holds arbitrary objects.
    '''

    def __init__(self, initial_size=10, chunk_size=5):
        '''Creates an array with an intial size.'''
        self.content = alloc(initial_size)
        self.size_alloc = initial_size
        self.size_filled = 0
        self.chunk_size = chunk_size


    def debug_print(self):
        '''Prints a representation of the entire allocated space, including unused spots.'''
        '''EX: 11 of 15 >>> a, e, r, o, I, o, d, u, s, a, u, null, null, null, null'''
        values = ', '.join(str(x) for x in self.content)
        print('{} of {} >>> {}'.format(
            self.size_filled, self.size_alloc, values))


    def _check_bounds(self, index):
        '''Ensures the index is within the bounds of the array: 0 <= index <= size.'''
        # Cant be less than 0, and cant be greater than the last index
        if index >= 0 and index <= self.size_filled - 1:
            return True
        else:
            print(IndexError('Index: {} out of bounds'.format(index)))
            return False

    def _check_increase(self):
        '''
        Checks whether the array is full and needs to increase by chunk size
        in preparation for adding an item to the array.
        '''
        if self.size_alloc == self.size_filled:
            # Set new size of allocated
            self.size_alloc = self.size_alloc + self.chunk_size
            # Allocate a new array
            temp_new_array = alloc(self.size_alloc)
            self.content = memcpy(temp_new_array, self.content, self.size_alloc)


    def _check_decrease(self):
        '''
        Checks whether the array has too many empty spots and can be decreased by chunk size.
        If a decrease is warranted, it should be done by allocating a new array and copying the
        data into it (don't allocate multiple arrays if multiple chunks need decreasing).
        '''
        empty_gap = self.size_alloc - self.size_filled
        if empty_gap >= self.chunk_size:
            # Set new size of allocated (Keeping array, just masking it to be shorter)
            self.size_alloc = self.size_alloc - self.chunk_size



    def add(self, item):
        '''Adds an item to the end of the array, allocating a larger array if necessary.'''
        self._check_increase()  # alloc more if needed
        self.content[self.size_filled] = item
        self.size_filled += 1


    def insert(self, index, item):
        '''Inserts an item at the given index, shifting remaining items right and allocating a larger array if necessary.'''


    def set(self, index, item):
        '''Sets the given item at the given index.  Throws an exception if the index is not within the bounds of the array.'''


    def get(self, index):
        '''Retrieves the item at the given index.  Throws an exception if the index is not within the bounds of the array.'''


    def delete(self, index):
        '''Deletes the item at the given index, decreasing the allocated memory if needed.  Throws an exception if the index is not within the bounds of the array.'''
        in_bounds = self._check_bounds(index)

        if in_bounds:
            self.content[index] = None
            self.size_filled -= 1
            # Iterate over array to right, starting one past index, and drop them down
            for i, item in enumerate(self.content[index + 1:], start=index + 1):
                self.content[i - 1] = item
            self._check_decrease()  # alloc less if needed


    def swap(self, index1, index2):
        '''Swaps the values at the given indices.'''


# Utilities
def alloc(size):
    '''
    Allocates array space in memory. This is similar to C's alloc function.
    '''
    new_array = [None] * size
    return new_array


def memcpy(dest, source, size):
    '''
    Copies items from one array to another.  This is similar to C's memcpy function.
    '''
    for index, item in enumerate(source):
        dest[index] = item

    return dest


def main(arguments):
    print('Test Array Checks------')

    test_array = Array()
    test_array.debug_print()

    for i in range(1):
        test_array.add('a')
        test_array.add('b')
        test_array.add('c')
        test_array.add('d')
        test_array.add('e')

    test_array.debug_print()
    for i in range(1):
        test_array.delete(2)
        test_array.debug_print()
        test_array.delete(3)
        test_array.debug_print()



if __name__ == '__main__':
    main(sys.argv[1:])
