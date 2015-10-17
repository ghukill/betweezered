# crumb server flask app

# python
import flask

'''
INSTALL FLASK SQL CONNECTOR
'''

# db related

# UNCOMMENT WITH FLASK SQL CONNECTOR ---------------------------------- #
# from flask import Flask, render_template, g
# from flask.ext.sqlalchemy import SQLAlchemy
# from sqlalchemy import create_engine, MetaData
# UNCOMMENT WITH FLASK SQL CONNECTOR ---------------------------------- #

# crumb
import localConfig

# create app
app = flask.Flask(__name__)
# UNCOMMENT WITH FLASK SQL CONNECTOR ---------------------------------- #
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://betweezered:betweezered@localhost/betweezered'

# #setup db
# db = SQLAlchemy(app)
# engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], convert_unicode=True)
# metadata = MetaData(bind=engine)
# db_con = engine.connect()
# UNCOMMENT WITH FLASK SQL CONNECTOR ---------------------------------- #

# get handlers
import views


