import operator

corpus = open('corpus_clean.txt')

def counting():
    characters = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    count = {' ': 0,'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0,
                 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0,
                 'X': 0, 'Y': 0, 'Z': 0}

    for letters in corpus.read():
        if letters in characters:
            count[letters] += 1

    total = float(sum(count.values()))

    for i in count:
        count[i] = count[i]/total

    freq = list(count.items())
    sorted_frequency = sorted(count.items(), key=operator.itemgetter(1), reverse=True)

    text = open('corpus_freq.txt', 'w+')
    for k,v in sorted_frequency:
        text.write("{}: {}".format(k,v) + '\n')
    text.close()

counting()