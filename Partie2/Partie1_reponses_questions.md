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
