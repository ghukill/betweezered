# crumb server flask app

# python
import flask


# db related
from flask import Flask, render_template, g
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData

# crumb
import localConfig

# create app
app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://betweezered:betweezered@localhost/betweezered'

#setup db
db = SQLAlchemy(app)
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], convert_unicode=True)
metadata = MetaData(bind=engine)
db_con = engine.connect()


def migrateDB():
	db.create_all()

# get handlers
import views
import models