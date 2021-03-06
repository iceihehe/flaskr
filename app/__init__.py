# -*- coding: utf-8 -*-

from flask import Flask

from config import DefaultConfig


def create_app(name=DefaultConfig.PROJECT):

    app = Flask(DefaultConfig.PROJECT)
    config_app(app)
    config_blueprints(app)

    return app


def config_app(app, config=None):

    app.config.from_object(DefaultConfig)

    if config:
        app.config.from_object(config)


def config_blueprints(app, blueprints=None):

    from .demo import demo

    app.register_blueprint(demo, url_prefix='/demo')
