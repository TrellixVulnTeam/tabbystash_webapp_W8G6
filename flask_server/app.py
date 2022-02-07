# from flask import Flask
# from flask_session import Session
# from flask_server.src.config import Config
# from flask_migrate import Migrate
# from blueprints.authentication import authentication  # , login_manager
# from flask_server.src.models import db
# from flask_cors import CORS
# import logging
# from src.config import ProdConfig


# sess = Session()  # create a session object (which connects to our redis session store and stores sessions in it)

# migrate = Migrate()


# def create_app():
#     app = Flask(__name__)

#     # configure our Flask app with an object that contains configuration variables
#     app.config.from_object(Config)

#     # let sqlalchemy know about and connect to our flask application
#     db.init_app(app)

#     sess.init_app(app)

#     # login_manager.init_app(app)

#     migrate.init_app(app, db)

#     app.register_blueprint(authentication)

#     return app
# from src import create_app
from src import create_app

# from src.config import ProdConfig

if __name__ == "__main__":
    app = create_app()
    # CORS(app, origins=["http://localhost:3000"])
    app.run()
