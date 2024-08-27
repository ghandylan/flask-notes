from flask import Flask, render_template
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

from blueprints import guest_bp, user_bp
from config import Config
from models import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    login_manager = LoginManager()
    login_manager.login_view = 'guest_views.login'
    login_manager.init_app(app)

    csrf = CSRFProtect()
    csrf.init_app(app)

    db.init_app(app)

    migrate = Migrate(app, db)
    migrate.init_app(app, db)

    app.register_blueprint(guest_bp.guest_blueprint)
    app.register_blueprint(user_bp.user_blueprint)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    @login_manager.user_loader
    def load_user(user_id):
        from models import User
        if User.query.get(user_id):
            return User.query.get(user_id)
        else:
            return None

    return app


app_instance = create_app()

if __name__ == '__main__':
    app_instance.run(threaded=True)
