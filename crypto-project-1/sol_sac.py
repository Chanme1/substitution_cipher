import operator

cipher = open('ciphertext.txt')

def ciphercount():
    characters = {}

    for char in cipher.read():
        characters[char] = characters.get(char,0) + 1

    total = float(sum(characters.values()))

    for i in characters:
        characters[i] = characters[i]/total

    freq = list(characters.items())
    sorted_frequency = sorted(characters.items(), key=operator.itemgetter(1), reverse=True)

    text = open('cipher_freq.txt', 'w+')
    for k,v in sorted_frequency:
        text.write("{}, {}".format(k,v) + '\n')
    text.close()

ciphercount()