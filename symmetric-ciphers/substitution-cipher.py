def encrypt(plaintext, key):
    CIPHER = list(key)
    ALPHABETIC = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    ciphertext = ''
    for i, l in enumerate(plaintext):
        index = ALPHABETIC.index(l);
        ciphertext += CIPHER[index];

    print plaintext, ' ---> ', ciphertext

def decrypt(ciphertext, key):
    CIPHER = list(key)
    ALPHABETIC = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    plaintext = ''
    for i, l in enumerate(ciphertext):
        index = CIPHER.index(l);
        plaintext += ALPHABETIC[index];

    print ciphertext, ' ---> ', plaintext

encrypt('HELLOWORLD', "ZEBRASCDFGHIJKLMNOPQTUVWXY")
decrypt('DAIILVLOIR', "ZEBRASCDFGHIJKLMNOPQTUVWXY")