#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A simple assignment 1, Part 2."""


class Book(object):
    """A book class."""

    author = " "

    title = " "

    def __init__(self, author, title):
        """Constructor for Book Class.

        Args:
            author (string): The author's name.
            title (string): The book title.
        """
        self.author = author
        self.title = title

    def display(self):
        """Prints title and author."""

        bookinfo = '"{}, written by {}"'.format(self.title, self.author)
        print bookinfo

book1 = Book('john Steinbeck', 'Of Mice and Men')

book2 = Book('Harper Lee', 'To Kill a Mockingbird')

book1.display()
book2.display()

            
