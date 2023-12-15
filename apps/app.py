from flask import Flask
from pathlib import Path
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
csrf = CSRFProtect()

# create_app 함수를 작성한다
def create_app():
    # 플라스크 인스턴스(객체)를 생성
    app = Flask(__name__)

# 앱의 config 설정을 한다
    app.config.from_mapping(
        SECRET_KEY="googlecloludplatform",
        SQLALCHEMY_DATABASE_URI=
        f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False ,
        WTF_CSRF_SECRET_KEY="AuwzyszU5sugKN7KZs6f")

    csrf.init_app(app)
    # SQL을 콘솔 로그에 출력하는 설정
    SQLALCHEMY_ECHO=True
    # SQLAlchemy와 앱을 연계한다
    db.init_app(app)
    # Migrate와 앱을 연계한다
    Migrate(app,db)
    # crud 패키지로부터 views를 import한다
    from apps.crud import views as crud_views
    # register_blueprint를 사용해 views의 crud를 앱에 등록한다
    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    return app

