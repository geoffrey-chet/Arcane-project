from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
import os

# Init app
app = Flask(__name__)
# BDD
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)

# Biens Class/Model
class Biens(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100),unique=True)
  description = db.Column(db.String(200))
  type = db.Column(db.String(50))
  ville= db.Column(db.String(50))
  caracteristiques= db.Column(db.String(200))
  proprietaire= db.Column(db.String(50))
  pieces= db.Column(db.Integer)
  def __init__(self,id, name, description, type, ville,caracteristiques,proprietaire,pieces):
    self.id=id
    self.name = name
    self.description = description
    self.type = type
    self.ville = ville
    self.caracteristiques = caracteristiques
    self.proprietaire= proprietaire
    self.pieces= pieces

# Schema biens
class BienSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'description', 'type', 'ville','caracteristiques','proprietaire','pieces')

# Init schema
biens_schema = BienSchema()
biens_schema = BienSchema(many=True)

# utilisateurs Class/Model
class Utilisateurs(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nom = db.Column(db.String(100))
  prenom= db.Column(db.String(100))
  date_naissance = db.Column(db.String(10))
  
  def __init__(self,id, nom, prenom, date_naissance):
    self.id=id
    self.nom = nom
    self.prenom = prenom
    self.date_naissance = date_naissance

# Schema utilisateurs
class UtilisateurSchema(ma.Schema):
  class Meta:
    fields = ('id', 'nom', 'prenom', 'date_naissance')

# Init schema
utilisateurs_schema = UtilisateurSchema()
utilisateurs_schema = UtilisateurSchema(many=True)

#Gestion des biens

# Creer un bien
@app.route('/biens', methods=['POST'])
def ajouter_bien():
  id=request.json['id']
  name = request.json['name']
  description = request.json['description']
  type = request.json['type']
  ville = request.json['ville']
  caracteristiques = request.json['caracteristiques']
  proprietaire = request.json['proprietaire']
  pieces = request.json['pieces']
  
  nouveau_bien=Biens(id,name,description,type,ville,caracteristiques,proprietaire,pieces)
  db.session.add(nouveau_bien)
  db.session.commit()

  return biens_schema.jsonify(nouveau_bien)

# Récupérer tous les biens
@app.route('/biens', methods=['GET'])
def recuperer_biens():
  afficher_biens = Biens.query.all()
  result = biens_schema.dump(afficher_biens)
  return jsonify(result)

# Afficher les biens d'une ville
@app.route('/biens/tri_par_ville/<ville>', methods=['GET'])
def afficher_biens_ville(ville):
  ville=str.capitalize(ville) #Ajoute une majuscule à la première lettre 
  afficher_biens = Biens.query.filter(Biens.ville==ville)
  result = biens_schema.dump(afficher_biens)
  return jsonify(result)

#Modifier un bien
@app.route('/biens/modifier/<id>', methods=['PUT'])
def modifier_bien(id):
  bien = Biens.query.get(id)

  name = request.json['name']
  description = request.json['description']
  type = request.json['type']
  ville = request.json['ville']
  caracteristiques = request.json['caracteristiques']
  proprietaire = request.json['proprietaire']
  pieces = request.json['pieces']

  bien.id=id
  bien.name = name
  bien.description = description
  bien.type = type
  bien.ville = ville
  bien.caracteristiques = caracteristiques
  bien.proprietaire = proprietaire
  bien.pieces = pieces

  db.session.commit()

  return biens_schema.jsonify(bien)

# Afficher un bien par id
@app.route('/biens/afficher/<id>', methods=['GET'])
def afficher_biens_id(id):
  afficher_biens = Biens.query.filter(Biens.id==id)
  result = biens_schema.dump(afficher_biens)
  return jsonify(result)
  
  
#Gestion utilisateurs

# Creer un bien
@app.route('/utilisateurs', methods=['POST'])
def ajouter_utilisateur():
  id=request.json['id']
  nom = request.json['nom']
  prenom = request.json['prenom']
  date_naissance = request.json['date_naissance']
  
  nouvel_utilisateur=Utilisateurs(id,nom,prenom,date_naissance)
  db.session.add(nouvel_utilisateur)
  db.session.commit()

  return biens_schema.jsonify(nouveau_bien)  
  
# Récupérer tous les utilisateurs
@app.route('/utilisateurs', methods=['GET'])
def recuperer_utilisateurs():
  afficher_utilisateurs = Utilisateurs.query.all()
  result = utilisateurs_schema.dump(afficher_utilisateurs)
  return jsonify(result)
  
#Modifier un utilisateur
@app.route('/utilisateurs/modifier/<id>', methods=['PUT'])
def modifier_utilisateur(id):
  utilisateur = Utilisateurs.query.get(id)

  nom = request.json['nom']
  prenom = request.json['prenom']
  date_naissance = request.json['date_naissance']

  utilisateur.id=id
  utilisateur.nom=nom
  utilisateur.prenom=prenom
  utilisateur.date_naissance=date_naissance

  db.session.commit()

  return biens_schema.jsonify(bien)


# Run Server
if __name__ == '__main__':
  app.run(debug=True)