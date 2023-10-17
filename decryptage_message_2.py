def dechiffrement_message_2(message_code, key):
    """
    Fonction qui déchiffre un message chiffré en utilisant le chiffrement Vigenère avec une clé donnée

    Args :
        message_code (String) : Le message codé
        key (String) : La clé utilisée pour le déchiffrement
    
    Return:
        resultat (String) : Le message déchiffré
    """
    resultat = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    longueur_cle = len(key)
    i = 0
    for lettre in range(len(message_code)):
        if message_code[lettre].isalpha():
            decalage = alphabet.index(key[i % longueur_cle])
            lettre = (alphabet.index(message_code[lettre]) - decalage) % 26
            resultat += alphabet[lettre]
            i += 1
        else:
            resultat += message_code[lettre]
    return resultat

# Message 2
message_2 = """AE IOW ZQBLXR WASIXQ WJR YKJ KGYUJAGY UU OXSLN TXRCUQYM
IY IRCTQ HPNF RR RQBIIIGOFN XQ WTCEKK DQ OIH MHXDUDQW BAYNVUDQYM
NR MRRPQD SU CXVMUQV HOHLWLQ CYT LRY GRQYMTRRY RPBMVXTVUES
QF EXNFO UEHAMAEM RV MQEWPGR IRCTQ HTREOVRQ XE HUOYKIFGXXOA"""

cle_message_1 = "PANGRAMME"
print(dechiffrement_message_2(message_2, cle_message_1))
