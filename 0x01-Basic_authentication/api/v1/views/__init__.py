#!/usr/bin/env python3
""" DocDocDocDocDocDoc
"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.index import *
from api.v1.views.users import *

<<<<<<< HEAD
User.load_from_file()
=======
# Ensure the User class is correctly imported from models.user
from models.user import User

User.load_from_file()
>>>>>>> 9fab7352010817c5002d55bf4d23499dc85d973a
