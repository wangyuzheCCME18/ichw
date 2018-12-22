"""wcount.py: Count words from an Internet file.

__author__ = "Wang Yuzhe"
__pkuid__  = "1800011828"
__email__  = "1800011828@pku.edu.cn"
"""

import sys
from urllib.request import urlopen


def w_count(lines, top_n=10):
    """Count words from lines of text string, then sort by their counts
    in reverse order, output the top_n (word count), each in one line."""
    word_count = {}  # Build a dictionary to count the words.
    for line in lines:
        for i in ['.', ',', '?', '!', ':', ';', '"', '\'']:  # Transform punctuation into blank.
            line = line.replace(i, ' ')
        line = line.split()  # Split the words.
        for word in line:
            word = word.lower()
            if word not in word_count:
                word_count[word] = 0
            else:
                word_count[word] += 1
    sorted_list = sorted(word_count.items(), key=lambda t: t[1], reverse=True)  # Sort the words by occurrence number.
    for i in range(0, min(top_n, len(sorted_list))):
        word, count = sorted_list[i]
        print(word, ' ' * (10 - len(word)), count)


def main():
    """Main module."""
    if len(sys.argv) == 1:  # No input, show the usage of the programme.
        print('Usage: {} url [top_n]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  top_n: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
    else:
        try:
            doc = urlopen(sys.argv[1])
        except Exception as error:
            error = str(error)
            if error == '<urlopen error [Errno 11001] getaddrinfo failed>':
                print('Sorry, the Internet connection is interrupted. Please try again. ')
                return
            if 'unknown url type' in error:
                print('Sorry, the url type is invalid. Please try again. ')
                return
            if error == 'HTTP Error 404: Not Found':
                print('Sorry, 404: the url is not found. Please try again. ')
                return
            else:
                print('Sorry, an unexpected error is raised. Please try again. ')
                return
        lines = ((doc.read()).decode('utf-8')).split('\r\n')
        doc.close()
        if len(sys.argv) == 2:  # Top_n not given.
            w_count(lines)
        elif len(sys.argv) == 3:  # Top_n given.
            top_n = int(sys.argv[2])
            w_count(lines, top_n=top_n)


if __name__ == '__main__':
    main()
