<style>
b { color: blue}
r { color: red}
a { color: aquamarine}
a1 {color: aqua}
</style>

# <r>SAE 3.09 : Cryptographie et sécurité</r>

# <b>Evann YANG Thomas RABILLON</b>

## Partie 1

## Questions

### 1. En supposant que RSA soit utilisé correctement, Eve peut-elle espérer en venir à bout? En vous appuyant sur votre cours, justifiez votre réponse.

En supposant que RSA soit utilisé correctement, Eve ne devrait pas pouvoir déchiffrer directement la communication. RSA repose sur la difficulté du problème de factorisation de grands nombres, ce qui signifie qu'il est extrêmement difficile de retrouver la clé privée à partir de la clé publique. Tant que les clés RSA sont suffisamment longues et bien générées, une attaque de force brute sur RSA serait impraticable en raison du temps nécessaire pour factoriser les grands nombres premiers utilisés dans les clés.

### 2. En quoi l’algorithme SDES est-il peu sécurisé? Vous justifierez votre réponse en analysant le nombre d’essai nécessaire à une méthode “force brute” pour retrouver la clé.

L'algorithme SDES est peu sécurisé principalement en raison de la taille de sa clé. Avec seulement 10 bits, une attaque par force brute serait relativement rapide. En utilisant une méthode de force brute, un attaquant devrait essayer 2^10 = 1024 clés possibles pour trouver la bonne. Aujourd'hui, cette taille de clé est considérée comme facilement vulnérable aux attaques.

### 3. Est-ce que double SDES est-il vraiment plus sur? Quelle(s) information(s) supplémentaire(s) Eve doit-elle récupérer afin de pouvoir espérer venir à bout du double DES plus rapidement qu’avec un algorithme brutal? Décrivez cette méthode astucieuse et précisez le nombre d’essai pour trouver la clé.

Le double SDES n'est pas nécessairement plus sûr s'il est utilisé avec des clés de taille similaire. Eve pourrait toujours utiliser une attaque de force brute en essayant toutes les combinaisons possibles de clés (2^10 \* 2^10 = 1 048 576 essais).

Pour rendre le double SDES plus sûr, ils pourraient utiliser des clés de taille plus importante. Si chaque clé est étendue à, par exemple, 16 bits, le nombre total de combinaisons devient 2^16 \* 2^16 = 4 294 967 296 essais. Cela rendrait l'attaque par force brute beaucoup plus difficile.

Cependant, il est important de noter que l'utilisation de clés plus longues augmente également la complexité et les ressources nécessaires pour le chiffrement et le déchiffrement. Les méthodes modernes recommandent l'utilisation d'une taille de clé beaucoup plus grande pour assurer la sécurité, et l'utilisation de DES ou ses variantes est obsolète en raison de la taille insuffisante des clés.

## Question-Code

## Partie 2

### 1. Est-ce vraiment un problème? Justifiez votre réponse.

Oui, la mise à jour du protocole vers l'utilisation de l'algorithme AES avec des clés de 256 bits crée des obstacles considérables pour Eve dans sa tentative de déchiffrer les communications entre Alice et Bob, car cela renforce la résistance à la force brute étant donné que les clés AES de 256 bits nécessitent une quantité astronomique de temps et de ressources pour être cassées par une attaque de force brute donc la robustesse accrue de la sécurité offerte par AES avec des clés de 256 bits est une mesure importante pour protéger la confidentialité des communications entre Alice et Bob et un probleme pour Eve.

### 2. La robustesse accrue de la sécurité offerte par AES avec des clés de 256 bits est une mesure importante pour protéger la confidentialité des communications :

#### 1. Le temps d’exécution du chiffrement/déchiffrement d’un message avec chacun des deux protocoles. Ici vous devez le mesurer expérimentalement et donc fournir le code Python associé.

Pour créer le code qui permet de chiffrer et déchiffrer un code avec le protocole AES nous avons implémenté les fonctions suivantes.

```python
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import padding
import os

# Générer une clé AES-256 bits de manière sécurisée
def generate_aes_key():
    password = b'your_secret_password'  # Remplacez par un mot de passe sécurisé
    salt = os.urandom(16)  # Génère une valeur aléatoire pour le sel
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # 256 bits
        salt=salt,
        iterations=100000,  # Choisissez un nombre approprié d'itérations
        backend=default_backend()
    )
    key = kdf.derive(password)
    return key


def encrypt_aes(msg, key):
    encryptor = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend()).encryptor()
    if isinstance(msg, str):
        msg = msg.encode('utf-8')  # Convertir la chaîne en octets

    # Ajouter du bourrage (padding)
    padder = padding.PKCS7(128).padder()
    padded_msg = padder.update(msg) + padder.finalize()

    return encryptor.update(padded_msg) + encryptor.finalize()

# Déchiffrer un message avec AES-256 bits
def decrypt_aes(msg, key):
    decryptor = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend()).decryptor()
    decrypted_msg = decryptor.update(msg) + decryptor.finalize()

    # Retirer le bourrage
    unpadder = padding.PKCS7(128).unpadder()
    unpadded_msg = unpadder.update(decrypted_msg) + unpadder.finalize()

    return unpadded_msg.decode('utf-8')

# Utiliser les fonctions
key_aes = generate_aes_key()
cipher_text = encrypt_aes("Bonjour chef", key_aes)
print(cipher_text)

plain_text = decrypt_aes(cipher_text, key_aes)
print(plain_text)
```

De plus pour comparer les temps de chiffrement et déchiffrement entre les deux protocoles nous avons utilisé le module time avec le code suivant :

```python
import time

message = "Bonjour chef"
cle = generate_aes_key()

# Mesurer le temps d'exécution du chiffrement AES
start_time = time.time()
cipher_aes = encrypt_aes(message, cle)
encryption_time_aes = time.time() - start_time
print("Temps d'exécution du chiffrage AES:", encryption_time_aes*1000)

# Mesurer le temps d'exécution du déchiffrement AES
start_time = time.time()
decipher_aes = decrypt_aes(cipher_aes, cle)
decryption_time_aes = time.time() - start_time
print("Temps d'exécution du déchiffrage AES:", decryption_time_aes*1000)

# Mesurer le temps d'exécution du chiffrement SDES
start_time = time.time()
cipher_sdes = chiffrer(0b110100001, 0b011011010, msg_to_list(message))
encryption_time_sdes = time.time() - start_time
print("Temps d'exécution du chiffrage SDES:", encryption_time_sdes*1000)

# Mesurer le temps d'exécution du déchiffrement SDES
start_time = time.time()
decipher_sdes = dechiffrer(0b110100001, 0b011011010, cipher_sdes)
decryption_time_sdes = time.time() - start_time
print("Temps d'exécution du déchiffrage SDES:", decryption_time_sdes*1000)
```

Ce qui nous donne :

```python
"Temps d'exécution du chiffrage AES: 0.17070770263671875"
"Temps d'exécution du déchiffrage AES: 0.3566741943359375"
"Temps d'exécution du chiffrage SDES: 0.6959438323974609"
"Temps d'exécution du déchiffrage SDES: 0.9150505065917969"
```

Nous pouvons voir une différence d'exécution entre les deux protocoles où le protocole AES est plus rapide.

#### 2.2 . Le temps de cassage d’AES (même pour un cassage astucieux) si vous deviez l’exécuter sur votre ordinateur. Ici il faut uniquement estimer le temps nécessaire (sinon vous ne pourriez pas rendre votre rapport à temps!). Vous préciserez votre configuration et vous fournirez le détail des calculs

Estimer le délai pour une attaque par force brute sur une clé AES-256 bits est extrêmement difficile en raison de la magnitude des calculs impliqués. La taille de l'espace des clés AES-256 est de 2²⁵⁶, ce qui est un nombre astronomique. Une estimation brute peut donner une idée approximative, mais cela reste une conjecture. Supposons qu'une machine puisse effectuer un milliard (10⁹) de tentatives de clés par seconde. Même avec cette énorme capacité de calcul, il faudrait encore 2²⁵⁶ /10⁹ secondes pour tester toutes les clés possibles. Cela équivaut à environ 3×10⁴³ années

### 3. Il existe d’autres types d’attaques que de tester les différentes possibilités de clés. Lesquelles? Vous donnerez une explication succincte de l’une d’elles

Il existe plusieurs types d'attaques cryptographiques autres que la simple force brute pour casser un système de chiffrement. L'une des attaques les plus connues est l'attaque par "analyse différentielle".

L'attaque par analyse différentielle exploite les variations dans le chiffrement des messages en fonction des changements dans l'entrée ou les clés. Elle implique l'observation de plusieurs paires de messages clairs et chiffrés pour identifier des modèles récurrents dans les différences (différentiels) entre eux. Ces différences peuvent fournir des indices sur la structure interne de l'algorithme de chiffrement.

Le processus de cette attaque implique la sélection de paires de messages clairs apparentés, la génération de différences entre les messages clairs et l'observation des différences résultantes dans les messages chiffrés. En analysant ces différences, un attaquant peut tenter de déduire des informations sur la clé secrète.

L'attaque par analyse différentielle est souvent plus efficace que la force brute, car elle exploite des faiblesses dans le processus de chiffrement lui-même. Cependant, elle nécessite une connaissance approfondie de l'algorithme de chiffrement spécifique et une quantité importante de paires de messages clairs et chiffrés pour être réalisée avec succès.

## Partie 3

