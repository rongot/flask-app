from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from  flask_marshmallow import Marshmallow
from flask_cors import CORS



db = SQLAlchemy()
ma=Marshmallow()
DB_NAME = "flask"



def create_app():
    app=Flask(__name__)
    CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:root@localhost:3306/{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from .react import react

    app.register_blueprint(react,url_prefix='/')

    from .module import Articals,ArticalsSchema

    

    with app.app_context():
        db.create_all()
    
    

    return app
