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
  name = db.Column(db.String(100), unique=True)
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
@app.route('/biens_par_ville/<ville>', methods=['GET'])
def afficher_biens_ville(ville):
  ville=str.capitalize(ville)
  afficher_biens = Biens.query.filter(Biens.ville==ville)
  result = biens_schema.dump(afficher_biens)
  return jsonify(result)


# Run Server
if __name__ == '__main__':
  app.run(debug=True)