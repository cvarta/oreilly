__author__ = 'chris'
"""
Lab 16, Objective 3:

This project builds on the previous one.

Copy your final.py file to a file named final2.py, then modify final2.py to print a histogram of the word lengths. A
histogram is a chart with columns whose heights correspond to the data they represent.

Below is an example of possible output from running the updated program with the declaration.txt file:


 Length    Count
       1       16
       2      267
       3      267
       4      169
       5      140
       6      112
       7       99
       8       68
       9       61
      10       56
      11       35
      12       13
      13        9
      14        7
      15        2

  400 -|
       |
       |
       |
       |
  300 -|
       |
       |   ******
       |   ******
       |   ******
  200 -|   ******
       |   ******
       |   *********
       |   ************
       |   ************
  100 -|   ***************
       |   ******************
       |   ************************
       |   ***************************
       |   ******************************
    0 -+-+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-
       | 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16


Hints for Program Design:
You don't need to be quite as sophisticated as the standard solution in your scaling and labeling, but you should
consider how to handle inputs where the counts are smaller (e.g. in the 5-50 range). The real trick is working out
what should be printed in each column for every row--it would be much easier to print the histogram sideways! (
meaning that's not an acceptable alternative).

Because our vertical (y-axis) scale is in increments of 20, we don't see representations of word lengths of fewer
occurrences than 20 (the 12- through 15-character words).

x-axis: length of words
y-axis: maximum count
"""


def word_length(filename):
    """
    >>> word_length("declaration.txt")
    Length Count
    1 16
    2 267
    3 267
    4 169
    5 140
    6 112
    7 99
    8 68
    9 61
    10 56
    11 35
    12 13
    13 9
    14 7
    15 2
    """

    try:
        f = open("declaration.txt", 'r')
        text = f.readlines()
        # Python removes the punctuation to ensure that only words are present in the text.
        #"It's" is not the same as "It's," # (with a comma), so the punctuation must be removed
        freq = {}
        for line in text:
            for punc in ",.?:;'\"-!&":
                line = line.replace(punc, "")
            #use the length as the key and the value for the count
            for word in line.split():
                freq[len(word)] = freq.get(len(word), 0) + 1

        print("Length Count")
        for word in sorted(freq.keys()):
            print(word, freq[word])

        # print the graph
        printGraph(freq)
    except FileNotFoundError:
        print("File Not found, check path/filename")


def printGraph(frequency):
    inverse = [(value, key) for key, value in frequency.items()]
    yScale = max(inverse)
    for row in range(0, 400, 20):
        for length in range(max(frequency)):
            if (length in frequency.keys() and frequency[length] >= row):
                print('*', end="")
        print()




def _test():
    import doctest, refactory

    return doctest.testmod(refactory)


if __name__ == "__main__":
    # _test()
    word_length("declaration.txt")