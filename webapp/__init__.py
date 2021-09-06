from flask import Flask  , render_template

from webapp.model import db 
from webapp.python_org_news import get_python_news
from webapp.weather import weather_by_city


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    db.init_app(app)

    @app.route("/")
    def index():
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'] , app.config['NUMBER_OF_WEATHER_DAYS'])
        tittle = "Новости Python"
        news_list =  get_python_news()

        return render_template("index.html ", page_tittle = tittle , weather = weather , news_list = news_list )

    return app

