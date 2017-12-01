# sol_cleaner.py cleans a file named corpus.txt.
# corpus.txt contains the text of chapter one from "Metamorphosis" by Franz Kafka

#import regular expression operations library
import re

#open corpus.txt file then reads and turns all the letters into uppercase
cipher = open('corpus.txt').read()
updated = cipher.upper()

remove = re.compile('[^a-zA-Z ]') #removes characters that are not within a-z or A-Z, and not a space
newcipher = remove.sub('', updated) #deletes those characters in the text

#creates a new text file called "corpus_clean.txt" with the output
text = open('corpus_clean.txt', 'w+')
text.write(newcipher)
text.close()