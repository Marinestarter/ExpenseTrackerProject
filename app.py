from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    migrate = Migrate(app, db)
    app.config.from_object('config.Config')

    db.init_app(app)
    import routes
    app.register_blueprint(routes.main)

    return app