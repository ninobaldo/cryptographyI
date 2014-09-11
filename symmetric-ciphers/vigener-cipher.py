def encrypt(plaintext, key):
    CIPHER = list(key)
    ALPHABETIC_LENGTH = 26
    ALPHABETIC = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    ciphertext = ''
    for i, l in enumerate(plaintext):
        plaintext_index = ALPHABETIC.index(l);
        key_index = ALPHABETIC.index(CIPHER[i % (len(key))])
        sum = plaintext_index + key_index

        ciphertext += ALPHABETIC[ sum % ALPHABETIC_LENGTH];

    print plaintext, ' ---> ', ciphertext

def decrypt(ciphertext, key):
    CIPHER = list(key)
    ALPHABETIC_LENGTH = 26
    ALPHABETIC = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    plaintext = ''
    for i, l in enumerate(ciphertext):
        ciphertext_index = ALPHABETIC.index(l);
        key_index = ALPHABETIC.index(CIPHER[i % (len(key))])
        sub = ciphertext_index - key_index

        plaintext += ALPHABETIC[ sub % ALPHABETIC_LENGTH];

    print ciphertext, ' ---> ', plaintext

encrypt('ATTACKATDAWN', "LEMONLEMONLE")
decrypt('LXFOPVEFRNHR', "LEMONLEMONLE")