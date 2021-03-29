from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config
import os
from dotenv import load_dotenv
load_dotenv()

db = SQLAlchemy()
migrate = Migrate()

def create_app(config=None):
    app = Flask(__name__)
    
    if app.config["ENV"] == 'production':
        # app.config.from_object('config.ProductionConfig')
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('URI')
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    else:
        app.config.from_object('config.DevelopmentConfig')

    if config is not None:
        app.config.update(config)

    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)

    from rookie_app.routes import (main_route, user_route, group_route)
    app.register_blueprint(main_route.bp)
    app.register_blueprint(user_route.bp, url_prefix='/api')
    app.register_blueprint(group_route.bp, url_prefix='/api')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
