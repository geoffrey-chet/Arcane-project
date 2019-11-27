# Arcane API REST

API  pour une application de gestion immobilière

## Récupération des fichiers depuis git

git clone https://github.com/geoffrey-chet/Arcane-project.git

## Installation des librairies

Accedez à la racine du projet avec une console python puis installez les librairies avec la commande suivante:
```
pip install -r requirements.txt
```

## Lancer l'API

Depuis une console Python:

```
py api.py
ou
python api.py
```

## Fonctionnalités

Consulter la liste des biens (méthode GET)

```
http://127.0.0.1:5000/biens
```

Ajouter un bien (méthode POST)

```
http://127.0.0.1:5000/biens

Exemple de bien à entrer:
{
    "caracteristiques": "Petit sejour et une grande chambre vue tour Eiffel", 
    "description": "36 metres carre", 
    "id": 255771, 
    "idproprietaire": 622282569, 
    "name": "Petit T2", 
    "pieces": 1, 
    "proprietaire": "Pascal Legrand", 
    "type": "T2", 
    "ville": "Paris"
  }
```

Modifier un bien (méthode PUT)

```
http://127.0.0.1:5000/biens/modifier/id_bien_à_modifier
exemple d'URL:
http://127.0.0.1:5000/biens/modifier/255771

et le JSON en entrée:

{
    "caracteristiques": "Caracteristiques modifiees", 
    "description": "36 metres carre", 
    "id": 255771, 
    "idproprietaire": 622282569, 
    "name": "Petit T2", 
    "pieces": 1, 
    "proprietaire": "Pascal Legrand", 
    "type": "T2", 
    "ville": "Paris"
  }
```

Consulter les biens d'une ville (méthode GET)
```
http://127.0.0.1:5000/biens/tri_par_ville/nom_de_la_ville
exemple:
http://127.0.0.1:5000/biens/tri_par_ville/paris
```

Consulter la liste des utilisateurs (méthode GET)

```
http://127.0.0.1:5000/utilisateurs
```

Ajouter un utilisateur (méthode POST)

```
http://127.0.0.1:5000/utilisateurs

Exemple d'utilisateur à entrer:
 {
    "date_naissance": "12/02/1967",
    "id": 3112512,
    "nom": "Cardefou",
    "prenom": "Paul"
  }
```

Modifier un utilisateur (méthode PUT)

```
http://127.0.0.1:5000/utilisateurs/modifier/id_utilisateur à modifier
exemple d'URL:
http://127.0.0.1:5000/utilisateurs/modifier/3112512

et le JSON en entrée:

{
    "date_naissance": "06/06/1966",
    "id": 3112512,
    "nom": "Cardefou",
    "prenom": "Paul"
  }
```

Un utilisateur peut modifier uniquement les caracteristiques de son bien (méthode PUT)
```
http://127.0.0.1:5000/utilisateurs/id_utilisateur/modifier/id_du_bien

Si le bien entrée à la fin de l'URL appartient à l'utilisateur entré, la modification est possible, sinon le message suivant apparait:"Action impossible, vous n'etes pas le proprietaire"

exemple d'URL acceptée avec les utilisateurs et biens déjà présents:
http://127.0.0.1:5000/utilisateurs/622282569/modifier/255771
exemple d'URL rejetée:
http://127.0.0.1:5000/utilisateurs/622282569/modifier/255770
```


