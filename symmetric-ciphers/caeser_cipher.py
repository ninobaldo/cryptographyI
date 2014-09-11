def encrypt(plaintext):
    ALPHABETIC = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    SHIFT = 3
    MAX_LENGTH = 25
    ALPHABETIC_LENGTH = 26
    ciphertext = ''
    for i, letter in enumerate(plaintext):
        it = ALPHABETIC.index(letter);
        index = (it + SHIFT) % ALPHABETIC_LENGTH;
        ciphertext += ALPHABETIC[index];

    print plaintext, ' ---> ', ciphertext


def decrypt(ciphertext):
    ALPHABETIC = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    SHIFT = 3
    MIN_LENGTH = 0
    ALPHABETIC_LENGTH = 26
    plaintext = ''
    for i, letter in enumerate(ciphertext):
        it = ALPHABETIC.index(letter);
        index = (it - SHIFT) % ALPHABETIC_LENGTH;

        plaintext += ALPHABETIC[index];
    print ciphertext, ' ---> ', plaintext


encrypt('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
decrypt('DEFGHIJKLMNOPQRSTUVWXYZABC')