# -*- coding: utf-8 -*-

from flask_admin import Admin

from .views import UserModelView
from app.models import User
from app.session import session


admin = Admin()
admin.add_view(UserModelView(User, session))
