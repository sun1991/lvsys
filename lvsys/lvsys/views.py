"""
Routes and views for the flask application.
"""

import json
from datetime import datetime
from flask import render_template
from lvsys import app
import util.lvdate
import util.thedate
import util.lvtype
import lvsys.db.lvdb as db


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/lv')
def lv():
    """render lv page."""
    all_lvdates = util.thedate.get_lvdates(2016)
    lv_types = [util.lvtype.LvType('mandatory', 1), util.lvtype.LvType('company', 2)]
    return render_template(
        'lv.html',
        lv_types = lv_types, # for template
        lv_types_json = json.dumps(lv_types, cls=util.lvtype.LvTypeEncoder),
        all_lvdates_json=json.dumps(all_lvdates, cls=util.lvdate.LvDateEncoder)
        )

@app.route('/test')
def test():
    import sqlite3
    import sys
    conn = sqlite3.connect('lvsys/db/lv.db')
    allusers = db.test_get_user(conn)
    print(allusers)

    return 'test'