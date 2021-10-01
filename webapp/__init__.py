from flask import Flask  , render_template , flash, redirect, url_for
from flask_login import current_user , LoginManager , login_required  

from webapp.model import db , News 

from webapp.user.models import User 
from webapp.user.views import blueprint as user_blueprint

from webapp.weather import weather_by_city


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    db.init_app(app) 

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    app.register_blueprint(user_blueprint)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
    
    @app.route("/")
    def index():
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'] , app.config['NUMBER_OF_WEATHER_DAYS'])
        tittle = "Новости Python"
        news_list =  News.query.order_by(News.published.desc()).all()

        
        return render_template("index.html ", page_tittle = tittle , weather = weather , news_list = news_list )

    
    @app.route('/admin')
    @login_required
    def admin_index():
        if current_user.is_admin:
            return 'Привет админ'
        else:
            return 'Ты не админ!'



    return app





