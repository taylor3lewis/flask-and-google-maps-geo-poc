# -*- coding: utf-8 -*-
# WebService for JobCrawler - Vr.: 1.0
from flask import Flask
from flask import render_template

# -------------------- #
# Flask Initialization #
# -------------------- #
app = Flask(__name__)
app.debug = False
app.config.from_object(__name__)


@app.route('/')
def index():
    """
    Index is a simply static HTML page, without dynamic infos,
    which provides only a list of links with the services routes
    :return: HTML Text
    """
    return render_template('index.html')


if __name__ == '__main__':
    try:
        app.run('localhost', threaded=True, port=3333)
    except Exception as ex:
        print ex