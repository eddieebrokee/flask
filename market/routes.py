from market import app
from flask import render_template
from market.model import Item

@app.route('/')
@app.route('/home')
def home():
    return render_template('base.html')


@app.route('/library')
def library():
    items = Item.query.all()
    return render_template('library.html',items = items)