from utils.get_config import *

### Texts
lag_text=f"""
:satellite: **Un lag a été constaté**, les <@&{to_id}> sont contactés.

:one: En attendant, chaque joueur peut :
:white_small_square: Vérifier qu'aucune autre connexion locale ne pompe la connexion.
:white_small_square: S'assurer que la connexion au réseau est, si possible, câblée.
:white_small_square: S'assurer qu'il/elle n'emploie pas un partage de connexion de réseau mobile (passable de DQ).

:two: Si malgré ces vérifications la connexion n'est pas toujours pas satisfaisante, chaque joueur doit :
:white_small_square: Préparer un test de connexion *(Switch pour Ultimate, Speedtest pour Project+)*.
:white_small_square: Décrire sa méthode de connexion actuelle *(Wi-Fi, Ethernet direct, CPL -> ADSL, FFTH, 4G...)*.

:three: Si nécessaire, un TO s'occupera de votre cas et proposera une arène avec le/les joueur(s) problématique(s).
"""

desync_text=f"""
:one: **Détecter une desync sur Project+ (Dolphin Netplay) :**
:white_small_square: Une desync résulte dans des inputs transmis au mauvais moment (l'adversaire SD à répétition, etc.).
:white_small_square: Si Dolphin affiche qu'une desync a été détectée, c'est probablement le cas.

:two: **Résoudre une desync, les 2 joueurs : **
:white_small_square: Peuvent avoir recours à une __personne de tierce partie__ pour déterminer le fautif.
:white_small_square: S'assurent qu'ils ont bien installé **la dernière version en date** de Project+.
:white_small_square: Vérifient depuis la fenêtre netplay que leur carte SD virtuelle a un hash MD5 égal à :
```
9b1bf61cf106b70ecbc81c1e70aed0f7
```
:white_small_square: Doivent vérifier que leur __ISO possède un hash MD5 inclus__ dans la liste compatible :
```
d18726e6dfdc8bdbdad540b561051087
d8560b021835c9234c28be7ff9bcaaeb
5052e2e15f22772ab6ce4fd078221e96
52ce7160ced2505ad5e397477d0ea4fe
9f677c78eacb7e9b8617ab358082be32
1c4d6175e3cbb2614bd805d32aea7311
```
*ISO : clic droit sur \"Super Smash Bros Brawl\" > Onglet \"Info\" > Ligne \"MD5 Checksum\".
SD : en haut à droite d'une fenêtre netplay, cliquer sur \"MD5 Check\" et choisir \"SD card\".*

:three: **Si ces informations ne suffisent pas, contactez un TO.**
"""
