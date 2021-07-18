from blankFlaskApp import db

#To be moved once module structure finalised.

class PostingCard:
    def ___init___(self, title, subTitle, imageURL):
        self.id = 0
        self.title = "Blank Card"
        self.subTitle = "This is a placeholder card"
        self.imageURL = "https://via.placeholder.com/400x600?text=CardImage"

    def generateCard(id, title, subTitle, imageURL):
        # Generates individual cards for display from input parameters.
        returnHtml = '<div class="carousel-item"><div class="card-title">'+ title +'</div><div class="card-body"><img class="d-block w-100" src="'+ imageURL + '" alt="Second Slide"></div><div class="card-subtitle">' + subTitle + '</div></div>'

        return returnHtml

# class PostDeck
    #Class for construction of post decks for display
#    def ___init___(self)
#        self.id = 0
#        self.deckArray[]

#    def populateArray()
#        return "none"
        

#####Database table models#####

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)

class Posting(db.Model):
    __tablename__ = 'posting'
    id = db.Column(db.Integer, primary_key=True)
    postName = db.Column(db.String(80), unique=True, nullable=False)
    location = db.Column(db.String(80), unique=False, nullable=False)

#class initDB:
    #Utility class to initialise a new database.