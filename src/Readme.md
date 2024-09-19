# Documentation Du Projet de Groupe 

---

Ce projet vise à etablir les bases pour la realisation du backend d'un forum

---

## Realiser par:

| Nom       | Prenom                 | Profil GitHub                                      |
| --------- | ---------------------- | -------------------------------------------------- |
| KONE      | KOLOTIOLOMAN DIEUDONNE | [kolo01](https://github.com/kolo01)                |
| DAGNOGO   | DONGUI                 | [DAGNOGO DONGUI](https://github.com/dagnogodongui) |
| SILUE     | IDRISSA                | [BoyStar](https://github.com/Boystar225)           |
| COULIBALY | ROKIA                  | [Rokia98](https://github.com/Rokia98)              |
| BERTHE    | HABIB                  | [StiBibo](https://github.com/StiBibo)              |

---

## Fonctionnalités

- #### Gestion des produits

#

            - Création d'un produit
            - Liste des produits
            - Modification du produit
            - suppression du produit

- #### Gestion du paiement

#

            - Ajout d'un moyen de paiement
            - Suppression d'un moyen de paiement
            - Modification d'un moyen de paiement

- #### Gestion des vendeur

#

            - Création d'un vendeur
            - Modification d'un vendeur
            - Suppression d'un vendeur

- #### Gestion de panier et des commandes

#

            - Ajout de produit au panier
            - suppression de produit dans le panier

---

## Comment executer notre application

- ### Prerequis

  Avoir `Python` installé sur sa machine, verifiable en tapant dans son terminal

  ```sh
  python --version
  ```

  Vous devez avoir un resultat similaire a cette ligne (la version peut ne pas etre la même)
  ![Imgur](https://i.imgur.com/EHqP7VE.png)

  - Si pas fait au préalable, vous pouvez télécharger le fichier d'installation sur [ le site officiel de PYTHON](https://www.python.org/downloads/)
    ![Imgur](https://i.imgur.com/A2iH1rj.png)
  - Avoir `Postgresql` installé sur sa machine , si vous l'avez pas, vous pouvez le telecharger [ICI](https://www.postgresql.org/download/)
  - Avoir `GIT` installé sur sa machine (`Optionnel`), si vous l'avez pas, vous pouvez le telecharger [ICI](https://git-scm.com/downloads)

### **_Tout ce qui suis doit être saisie dans le terminal_**

- > #### Creer l'environnement virtuel avec
  #
  ```sh
  python -m venv env
  ```
- > #### Activer son environnement virtuel

  #

  (windows)

  ```sh
  .\env\Scripts\activate
  ```

  (macos)

  ```sh
  source env/bin/activate
  ```

- > #### Telecharger le projet avec [ce lien](https://github.com/kolo01/EcommerceV1/archive/refs/heads/main.zip) ou avec la commande

  #

  ```sh
  git clone https://github.com/kolo01/EcommerceV1.git
  ```

  ###

  ```sh
  pip install -r requirements.txt
  ```

- > #### On s'assure d'avoir creer une base de donnée dans Postegresql et on verifie la configuration dans le fichier settings.py contenu dans le dossier forum.
  >
  > **_Un exemple de configurations_** > ![Imgur](https://i.imgur.com/zmFELG2.png)

- > #### On lance nos migrations avec

  ###

  ```sh
      python manage.py makemigrations
  ```

  ```sh
      python manage.py migrate
  ```

- > #### On lance notre projet
  ###
  ```sh
  python manage.py runserver
  ```
- > #### On va dans le navigateur et on tape
  ###
  ```sh
  http://127.0.0.1:8000/api
  ```
