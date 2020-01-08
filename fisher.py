'''
fisher Create by wangxiaoming on 2019/12/26.
'''
from flask import Flask

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run('0.0.0.0', debug=app.config['DEBUG'], port=5000)
