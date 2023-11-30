from sys import exit
from time import time
 
KeyLength = 10
SubKeyLength = 8
DataLength = 8
FLength = 4
 
# Tables for initial and final permutations (b1, b2, b3, ... b8)
IPtable = (2, 6, 3, 1, 4, 8, 5, 7)
FPtable = (4, 1, 3, 5, 7, 2, 8, 6)
 
# Tables for subkey generation (k1, k2, k3, ... k10)
P10table = (3, 5, 2, 7, 4, 10, 1, 9, 8, 6)
P8table = (6, 3, 7, 4, 8, 5, 10, 9)
 
# Tables for the fk function
EPtable = (4, 1, 2, 3, 2, 3, 4, 1)
S0table = (1, 0, 3, 2, 3, 2, 1, 0, 0, 2, 1, 3, 3, 1, 3, 2)
S1table = (0, 1, 2, 3, 2, 0, 1, 3, 3, 0, 1, 0, 2, 1, 0, 3)
P4table = (2, 4, 3, 1)
 
def perm(inputByte, permTable):
    """Permute input byte according to permutation table"""
    outputByte = 0
    for index, elem in enumerate(permTable):
        if index >= elem:
            outputByte |= (inputByte & (128 >> (elem - 1))) >> (index - (elem - 1))
        else:
            outputByte |= (inputByte & (128 >> (elem - 1))) << ((elem - 1) - index)
    return outputByte
 
def ip(inputByte):
    """Perform the initial permutation on data"""
    return perm(inputByte, IPtable)
 
def fp(inputByte):
    """Perform the final permutation on data"""
    return perm(inputByte, FPtable)
 
def swapNibbles(inputByte):
    """Swap the two nibbles of data"""
    return (inputByte << 4 | inputByte >> 4) & 0xff
 
def keyGen(key):
    """Generate the two required subkeys"""
    def leftShift(keyBitList):
        """Perform a circular left shift on the first and second five bits"""
        shiftedKey = [None] * KeyLength
        shiftedKey[0:9] = keyBitList[1:10]
        shiftedKey[4] = keyBitList[0]
        shiftedKey[9] = keyBitList[5]
        return shiftedKey
 
    # Converts input key (integer) into a list of binary digits
    keyList = [(key & 1 << i) >> i for i in reversed(range(KeyLength))]
    permKeyList = [None] * KeyLength
    for index, elem in enumerate(P10table):
        permKeyList[index] = keyList[elem - 1]
    shiftedOnceKey = leftShift(permKeyList)
    shiftedTwiceKey = leftShift(leftShift(shiftedOnceKey))
    subKey1 = subKey2 = 0
    for index, elem in enumerate(P8table):
        subKey1 += (128 >> index) * shiftedOnceKey[elem - 1]
        subKey2 += (128 >> index) * shiftedTwiceKey[elem - 1]
    return (subKey1, subKey2)
 
def fk(subKey, inputData):
    """Apply Feistel function on data with given subkey"""
    def F(sKey, rightNibble):
        aux = sKey ^ perm(swapNibbles(rightNibble), EPtable)
        index1 = ((aux & 0x80) >> 4) + ((aux & 0x40) >> 5) + \
                 ((aux & 0x20) >> 5) + ((aux & 0x10) >> 2)
        index2 = ((aux & 0x08) >> 0) + ((aux & 0x04) >> 1) + \
                 ((aux & 0x02) >> 1) + ((aux & 0x01) << 2)
        sboxOutputs = swapNibbles((S0table[index1] << 2) + S1table[index2])
        return perm(sboxOutputs, P4table)
 
    leftNibble, rightNibble = inputData & 0xf0, inputData & 0x0f
    return (leftNibble ^ F(subKey, rightNibble)) | rightNibble
 
def encrypt(key, plaintext):
    """Encrypt plaintext with given key"""
    data = fk(keyGen(key)[0], ip(plaintext))
    return fp(fk(keyGen(key)[1], swapNibbles(data)))
 
def decrypt(key, ciphertext):
    """Decrypt ciphertext with given key"""
    data = fk(keyGen(key)[1], ip(ciphertext))
    return fp(fk(keyGen(key)[0], swapNibbles(data)))  
 
# if __name__ == '__main__':
#     # Test vectors described in "Simplified DES (SDES)"
#     # (http://www2.kinneret.ac.il/mjmay/ise328/328-Assignment1-SDES.pdf)
 
#     try:
#         assert encrypt(0b0000000000, 0b10101010) == 0b00010001
#     except AssertionError:
#         print("Error on encrypt:")
#         print("Output: ", encrypt(0b0000000000, 0b10101010), "Expected: ", 0b00010001)
#         exit(1)
#     try:
#         assert encrypt(0b1110001110, 0b10101010) == 0b11001010
#     except AssertionError:
#         print("Error on encrypt:")
#         print("Output: ", encrypt(0b1110001110, 0b10101010), "Expected: ", 0b11001010)
#         exit(1)
#     try:
#         assert encrypt(0b1110001110, 0b01010101) == 0b01110000
#     except AssertionError:
#         print("Error on encrypt:")
#         print("Output: ", encrypt(0b1110001110, 0b01010101), "Expected: ", 0b01110000)
#         exit(1)
#     try:
#         assert encrypt(0b1111111111, 0b10101010) == 0b00000100
#     except AssertionError:
#         print("Error on encrypt:")
#         print("Output: ", encrypt(0b1111111111, 0b10101010), "Expected: ", 0b00000100)
#         exit(1)
 
#     t1 = time()
#     for i in range(1000):
#         encrypt(0b1110001110, 0b10101010)
#     t2 = time()
#     print("Elapsed time for 1,000 encryptions: {:0.3f}s".format(t2 - t1))
#     exit()


def sdes_encrypt_block(key1, key2, plaintext):
    """Fonction qui chiffre deux fois un bloc de 8 bits avec SDES soit deux clés

    Args:
        key (str): Clé de chiffrement
        plaintext (str): Bloc de 8 bits à chiffrer

    Returns:
        str:    Bloc de 8 bits chiffré
    """
    # Convertir la chaîne binaire en entier pour l'opération de chiffrement
    plaintext_int = int(plaintext, 2)
    # Chiffrer le bloc
    ciphertext_int = encrypt(int(key1, 2), plaintext_int)
    ciphertext_int = encrypt(int(key2, 2), ciphertext_int)

    # Convertir le résultat chiffré en chaîne binaire
    ciphertext_block = format(ciphertext_int, '08b')
    return ciphertext_block

def sdes_decrypt_block(key1, key2, ciphertext):
    """Fonction qui déchiffre un bloc de 8 bits avec SDES soit deux clés

    Args:
        key1 (str):  Clé de chiffrement
        key2 (str):  Clé de chiffrement
        ciphertext (str):   Bloc de 8 bits à déchiffrer

    Returns:
        str:    Bloc de 8 bits déchiffré
    """
    # Convertir la chaîne binaire en entier pour l'opération de déchiffrement
    ciphertext_int = int(ciphertext, 2)
    # Déchiffrer le bloc
    plaintext_int = decrypt(int(key1, 2), ciphertext_int)
    plaintext_int = decrypt(int(key2, 2), plaintext_int)
    # Convertir le résultat déchiffré en chaîne binaire
    plaintext_block = format(plaintext_int, '08b')
    return plaintext_block


def cassage_brutal(message_clair, message_chiffre):
    """Fonction de cassage brutal d'un message chiffré avec SDES et qui retourne les combinaison de clés possibles

    Args:
        message_clair (str):    Message clair
        message_chiffre (str):  Message chiffré

    Returns:
        liste: liste des double clés possibles   
    """
    # Générer toutes les clés possibles
    keys = []
    resultat = []
    for i in range(1024):
        key = format(i, '010b')
        keys.append(key)
    # Chiffrer le message clair avec toutes les clés possibles
    keys2 = keys.copy()
    for key1 in keys:
        for key2 in keys2:
            ciphertext = ""
            for i in range(0, len(message_clair), 8):
                plaintext_block = message_clair[i:i+8]
                ciphertext_block = sdes_encrypt_block(key1,key2, plaintext_block)
                ciphertext += ciphertext_block
            # Vérifier si le message chiffré correspond au message chiffré donné
            if ciphertext == message_chiffre and (key1,key2) not in resultat and sdes_decrypt_block(key2,key1, ciphertext) == message_clair:
                resultat.append((key1,key2))
    return resultat


key1 = "0111111101"
key2 = "1010100111"
plaintext_block = "10010111"
ciphertext_block = sdes_encrypt_block(key1,key2, plaintext_block)
decrypted_block = sdes_decrypt_block(key2,key1, ciphertext_block)


print("Test Cassage_brutal:")
print("clé1:", key1)
print("clé2:", key2)
print("Plaintext Block:", plaintext_block)
print("Ciphertext Block:", ciphertext_block)
print("Decrypted Block:", decrypted_block)
print("Cassage_brutal:", cassage_brutal(plaintext_block, ciphertext_block))
print()

def cassage_astucieux(message_clair, message_chiffre):
    """Fonction qui teste moins de possibilités de clés et réduit le temps d'exécution du cassage

    Args:
        message_clair (str):    Message clair
        message_chiffre (str):  Message chiffré

    Returns:
        list: Liste des paires de clés possibles
    """
    # Générer toutes les clés possibles
    keys = []
    resultat = []
    for i in range(1024):
        key = format(i, '010b')
        keys.append(key)
    # Chiffrer le message clair avec toutes les clés possibles
    keys2 = keys.copy()
    keys3 = keys.copy()
    keys3.reverse()
    keys4 = keys.copy()
    keys4.reverse()
    for key1 in keys:
        for key2 in keys2:
            ciphertext = ""
            texte2 = ""
            for i in range(0, len(message_clair), 8):
                plaintext_block = message_clair[i:i+8]
                ciphertext_block = sdes_encrypt_block(key1,key2, plaintext_block)
                ciphertext += ciphertext_block
                plaintext_block = message_clair[i:i+8]
                ciphertext_block2 = sdes_encrypt_block(key3,key4, plaintext_block)
                texte2 += ciphertext_block2
            # Vérifier si le message chiffré correspond au message chiffré donné
            if ciphertext == message_chiffre and (key1,key2) not in resultat and sdes_decrypt_block(key2,key1, ciphertext) == message_clair:
                resultat.append((key1,key2))
    return resultat

    

# Exemple d'utilisation
key1 = "0111111101"
key2 = "1010100111"
plaintext_block = "10010111"
ciphertext_block = sdes_encrypt_block(key1, key2, plaintext_block)
decrypted_block = sdes_decrypt_block(key2, key1, ciphertext_block)

# print("Test Cassage_astucieux:")
# print("clé1:", key1)
# print("clé2:", key2)
# print("Plaintext Block:", plaintext_block)
# print("Ciphertext Block:", ciphertext_block)
# print("Decrypted Block:", decrypted_block)
# print("Cassage_astucieux:", cassage_astucieux(plaintext_block, ciphertext_block))
