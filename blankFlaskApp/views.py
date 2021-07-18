"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template

from blankFlaskApp import app
from blankFlaskApp import model
from blankFlaskApp import db

#Fucking about with SQLAlchemy

db.create_all() # Use only to init DB

db.session.add(model.Posting(id="0", postName="Dogsbody Generic Manpower SAC 345", location="90 Signals Unit"))
db.session.commit()

#End of shitshow

@app.route('/')
@app.route('/home')
def home():
    """Perform Data Collection"""
    cardNO1 = model.PostingCard.generateCard(0, "90 Signals Unit (RAF Leeming)" , 'Dogsbody Generic Manpower SAC 345' , "https://via.placeholder.com/468x300?text=Card" )

    """Renders the home page."""
    return render_template(
        'index.html',
        title='POSTIN',
        year=datetime.now().year,
        card=cardNO1,
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
