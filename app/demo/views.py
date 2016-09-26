# -*- coding: utf-8 -*-

from flask import make_response
from flask.views import MethodView


class IndexView(MethodView):

    def get(self):

        return make_response('Congratulations!')
