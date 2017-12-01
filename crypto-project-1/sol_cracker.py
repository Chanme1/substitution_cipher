#sol_cracker.py opens the two file we compiled from sol_sap.py, and sol_sac.py
#The frequency found is used to decrypt the original ciphertext

cipher = open('ciphertext.txt').read()
cipherfreq = open('cipher_freq.txt').read()
corpusfreq = open('corpus_freq.txt').read()

#takes the first character of each line and puts it into key and Letters
with open('corpus_freq.txt') as corpusfreq:
    key = (''.join(line[0]for line in corpusfreq if line))

with open('cipher_freq.txt') as cipherfreq:
    Letters = (''.join(line[0]for line in cipherfreq if line))

#decrypts the ciphertext

translation = ""
a = str(key)
b = str(Letters)
a, b = b, a

for char in cipher:
    if char in a:
        charindex = a.find(char)
        translation += b[charindex]

#writes the output into a new file
text = open ("cracked.txt", "w+")
text.write(translation)
text.close()


