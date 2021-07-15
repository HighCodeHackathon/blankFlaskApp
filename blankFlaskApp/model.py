class PostingCard:
    def ___init___(self, title, subTitle, imageURL):
        self.title = "Blank Card"
        self.subTitle = "This is a placeholder card"
        self.imageURL = "https://via.placeholder.com/400x600?text=CardImage"

    def generateCard(title, subTitle, imageURL):
        # Generates individual cards for display from input parameters.
        returnHtml = '<div class="carousel-item"><div class="card-title">'+ title +'</div><div class="card-body"><img class="d-block w-100" src="'+ imageURL + '" alt="Second Slide"></div><div class="card-subtitle">' + subTitle + '</div></div>'

        return returnHtml