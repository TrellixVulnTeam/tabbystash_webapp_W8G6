from flask import Flask, current_app
from src.extensions import sess, db, migrate, cors#, login_manager
from src.config import Config 
from src.auth import bp as auth_bp
from src.models import User
#from src.auth.emailpassword import login_manager
from flask_login import LoginManager

def create_app():
    app = Flask(__name__)

    # configure our Flask app with an object that contains configuration variables
    app.config.from_object(Config)

    # let sqlalchemy know about and connect to our flask application, and then create the tables in the database if they're not already created
    db.init_app(app)
    with app.app_context():
        db.create_all()

    sess.init_app(app)

    
    login_manager = LoginManager()

    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        #from pudb import set_trace; set_trace()
        print('WHY IS THIS NOT WORKING')
        return User.query.get(int(id))

    

    migrate.init_app(app, db)

    app.register_blueprint(auth_bp)

    cors.init_app(app, origins=['http://localhost:3000'], supports_credentials=True)

    #_configureEmailServer()

    return app
