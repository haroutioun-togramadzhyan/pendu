import pygame
import random
import sys

# Initialisation de Pygame
pygame.init()

# Paramètres du jeu
largeur, hauteur = 800, 600
ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Jeu du Pendu")

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)

# Chargement des mots depuis le fichier "mots.txt"
with open("mots.txt", "r") as fichier_mots:
    mots = fichier_mots.read().splitlines()

# Chargement/sauvegarde des scores
scores = []

# Fonction pour choisir un mot aléatoire
def choisir_mot():
    return random.choice(mots).upper()

# Fonction pour dessiner le pendu
def dessiner_pendu(erreurs):
    if erreurs >= 1:
        pygame.draw.circle(ecran, noir, (150, 150), 30)  # Tête
    if erreurs >= 2:
        pygame.draw.line(ecran, noir, (150, 180), (150, 300), 5)  # Corps
    if erreurs >= 3:
        pygame.draw.line(ecran, noir, (150, 200), (100, 250), 5)  # Bras gauche
    if erreurs >= 4:
        pygame.draw.line(ecran, noir, (150, 200), (200, 250), 5)  # Bras droit
    if erreurs >= 5:
        pygame.draw.line(ecran, noir, (150, 300), (100, 350), 5)  # Jambe gauche
    if erreurs >= 6:
        pygame.draw.line(ecran, noir, (150, 300), (200, 350), 5)  # Jambe droite

# Fonction pour afficher le mot à deviner
def afficher_mot(mot, lettres_devinées):
    font = pygame.font.Font(None, 36)
    texte_mot = font.render(" ".join(lettres_devinées), True, noir)
    ecran.blit(texte_mot, (largeur // 2 - texte_mot.get_width() // 2, hauteur // 2 - 50))

# Fonction pour afficher les lettres déjà proposées
def afficher_lettres_proposées(lettres_proposées):
    font = pygame.font.Font(None, 24)
    texte_lettres = font.render("Lettres proposées : {}".format(", ".join(lettres_proposées)), True, noir)
    ecran.blit(texte_lettres, (20, 20))

# Fonction pour afficher le pendu et le mot
def afficher_interface(erreurs, mot, lettres_devinées, lettres_proposées):
    ecran.fill(blanc)
    dessiner_pendu(erreurs)
    afficher_mot(mot, lettres_devinées)
    afficher_lettres_proposées(lettres_proposées)
    pygame.display.flip()

# Fonction principale du jeu
def jouer():
    mot_a_deviner = choisir_mot()
    lettres_devinées = ["_" for _ in mot_a_deviner]
    lettres_proposées = []
    erreurs = 0

    # Boucle principale
    while True:
        afficher_interface(erreurs, mot_a_deviner, lettres_devinées, lettres_proposées)

        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    lettre_proposée = event.unicode.upper()
                    if lettre_proposée not in lettres_proposées:
                        lettres_proposées.append(lettre_proposée)
                        if lettre_proposée in mot_a_deviner:
                            for i, lettre in enumerate(mot_a_deviner):
                                if lettre == lettre_proposée:
                                    lettres_devinées[i] = lettre
                        else:
                            erreurs += 1

        # Vérifier si le joueur a gagné ou perdu
        if "_" not in lettres_devinées:
            print("Félicitations, vous avez trouvé le mot : {}".format(mot_a_deviner))
            # Ajoutez ici la logique pour enregistrer le score
            break
        elif erreurs >= 6:
            print("Désolé, vous avez perdu. Le mot était : {}".format(mot_a_deviner))
            # Ajoutez ici la logique pour enregistrer le score
            break

# Lancer le jeu
jouer()
