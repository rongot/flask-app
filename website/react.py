from flask import Blueprint, Flask, make_response,request,jsonify
from . import db
from .module import Articals, ArticalsSchema

aricale_schema=ArticalsSchema()
aricales_schema=ArticalsSchema(many=True)

react=Blueprint('react',__name__)

@react.route('/')
def index():
    return jsonify({"hellow":"world"})

@react.route('/get',methods=["GET"])
def get_articles():
    all_articals=Articals.query.all()
    results=aricales_schema.dump(all_articals)
    return jsonify(results)

@react.route('/get/<id>',methods=["GET"])
def post_details(id):
    articale=Articals.query.get(id)
    return aricale_schema.jsonify(articale)

@react.route('/add',methods=['Post'])
def add_article():
    title=request.json['title']
    body=request.json['body']

    articals=Articals(title=title,body=body)
    db.session.add(articals)
    db.session.commit()
    # print(aricale_schema.loads(articals))
    return aricale_schema.jsonify(articals)

@react.route('/update/<id>',methods=["PUT"])
def update_article(id):
    articale=Articals.query.get(id)

    title=request.json['title']
    body=request.json['body']

    articale.title=title
    articale.body=body
    # db.session.add(articale)
    print(articale)
    db.session.commit()
    return aricale_schema.jsonify(articale)

@react.route('/delete/<id>',methods=["DELETE"])
def delete_article(id):
    articale=Articals.query.get(id)
    db.session.delete(articale)
    db.session.commit()
    return aricale_schema.jsonify(articale)

