# -*- coding: utf-8 -*-

from flask import Blueprint

from .views import IndexView


demo = Blueprint('demo', __name__)

demo.add_url_rule('/', view_func=IndexView.as_view('demo_index'))
