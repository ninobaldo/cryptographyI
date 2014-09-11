def caeser_cipher_encrypt(plaintext):
    ALPHABETIC = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    SHIFT = 3
    MAX_LENGTH = 25
    ALPHABETIC_LENGTH = 26
    ciphertext = ''
    for i, letter in enumerate(plaintext):
        it = ALPHABETIC.index(letter);
        index = it + SHIFT;

        if index > MAX_LENGTH:
            index = index - ALPHABETIC_LENGTH;

        ciphertext += ALPHABETIC[index];
    print plaintext, ' ---> ', ciphertext

def caeser_cipher_decrypt(ciphertext):
    ALPHABETIC = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    SHIFT = 3
    MIN_LENGTH = 0
    ALPHABETIC_LENGTH = 26
    plaintext = ''
    for i, letter in enumerate(ciphertext):
        it = ALPHABETIC.index(letter);
        index = it - SHIFT;

        if index < MIN_LENGTH:
            index = index + ALPHABETIC_LENGTH;

        plaintext += ALPHABETIC[index];
    print ciphertext, ' ---> ', plaintext



caeser_cipher_encrypt('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
caeser_cipher_decrypt('DEFGHIJKLMNOPQRSTUVWXYZABC')