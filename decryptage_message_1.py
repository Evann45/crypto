def dechiffrement_message1(message_code, decalage):
    """
    Fonction qui permet de déchiffrer un message chiffré avec le chiffrement de César

    Args :
        message_code (String) : Le message chiffré
        decalage (int) : Le décalage utilisé pour le chiffrement
    
    Return:
        resultat (String) : Le message déchiffré
    """
    resultat = ""
    alphabet = {lettre: i for i, lettre in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}

    for lettre in message_code:  
        if lettre.isalpha():  
            index = (alphabet[lettre] + decalage) % 26
            for cle, valeur in alphabet.items():  
                if valeur == index: 
                    lettre_decrypte = cle 
                    break
        else:
            lettre_decrypte = lettre  
        resultat += lettre_decrypte
    return resultat


def combinaison_possible_cesar(message_code):
    """
    Fonction qui permet de déchiffrer un message chiffré avec le chiffrement de César avec toute les combinaisons possibles

    Args :
        message_code (String) : Le message chiffré
    """
    for nb in range(27):
        message = dechiffrement_message1(message_code, nb)
        print("décalage de ", nb + 1, ": ", message) 



message_a_dechiffrer = """BDQE PG OTQYUZ EQ OMOTQ GZ FDQEAD
MOODAOTQ M GZ MDNDQ FAGF DQOAGHQDF P'AD
ZQ ZQSXUSQ BME XM VQGZQ BAGOQ RQGUXXG
SDMZP QEF EAZ EQODQF YMXSDQ EM FMUXXQ YQZGQ
DAZPQE QF OAXADQQE EAZF XQE NMUQE CG'UX BADFQ
MZUEQQE QF EGODQQE, XQGDE EMHQGDE EAZF RADFQE.
YMUE MFFQZFUAZ M ZQ BME XQE ODACGQD,
YQYQ EU XM RMUY FUDMUXXQ FQE QZFDMUXXQE,
QZ MGOGZ OME FG ZQ PAUE EGOOAYNQD
"""


# Appel de la fonction de combinaison_possible_cesar pour tous les décalages possibles
combinaison_possible_cesar(message_a_dechiffrer)

# Appel de la fonction de dechiffrement_message1 pour une valeur donnée
print(dechiffrement_message1(message_a_dechiffrer, 14))
