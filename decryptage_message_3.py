def trouve_cle_alphabet(message_code):
    """
    Fonction qui permet de trouver les caractères uniques dans le message et les stocke dans une liste pour former un alphabet
    Args:
        message_code (str): Message à déchiffrer
    Returns:
        resultat: Liste de caractères représentant un alphabet
    """
    lettre_vu = set() 
    resultat = [] 
    for indice in range(len(message_code)): 
        if message_code[indice] != " " and message_code[indice] not in lettre_vu: 
            lettre_vu.add(message_code[indice])
            resultat.append(message_code[indice]) 
    return resultat

def decode_message_3(cle):
    """
    Fonction qui permet de déchiffre un message à l'aide de l'alphabet donné
    Args:
        cle (list): Liste représentant l'alphabet initial
    """
    for indice in range(26):  
        if indice == 0:
            cle.insert(indice, "Y")  
        else:
            cle.pop(indice - 1)  
            cle.insert(indice, "Y")  
        print("index :", indice)
        print(decode_message_3_bis(message_code, cle), "\n")  

def decode_message_3_bis(message_code, cle):
    """
    Fonction qui permet de déchiffre un message à l'aide de l'alphabet donné
    Args:
        message_code (str): Message à déchiffrer
        cle (list): Liste représentant l'alphabet initial
    Returns:
        resultat (str): Message déchiffré
    """
    resultat = '' 
    for lettre in message_code: 
        if lettre in cle:  
            index = cle.index(lettre)  
            resultat += chr(index + 65) # 65 est le code ASCII de A 
        else:
            resultat += lettre 
    return resultat


message_code = "EALOK, OKCT LOFX PLPSF! BF VKIF L ZKCASRA FTD: FBRXFEFDH"
cle = trouve_cle_alphabet("""LE VIF ZEPHIR JUBILE SUR LES KUMQUATS DU CLOWN GRACIEUX""")

print(decode_message_3(cle))
# Le bon message décodé dans tout les prints affiché dans le terminal est à l'index 12: 
# BRAVO, VOUS AVEZ GAGNE! LE CODE A FOURNIR EST: ELIZEBETH 