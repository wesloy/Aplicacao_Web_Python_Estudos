#importações básicas do framework
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server

#CRIAR APP
app = Flask(__name__)
app.config.from_object('config')

# SISTEMA DE LOGIN
lm = LoginManager()
lm.login_view = 'login'
lm.init_app(app)

# BANCO DE DADOS
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)


from sentinella.models import forms, tables
from sentinella.controllers import routes
