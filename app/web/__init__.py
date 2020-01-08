'''
__init__ Create by wangxiaoming on 2019-12-27.
'''
from flask import Blueprint

web = Blueprint('web',__name__)

from app.web import book
from app.web import user