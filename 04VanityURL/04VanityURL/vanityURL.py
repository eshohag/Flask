from app import app;


@app.route('/')
def intro():
    """Renders a sample page."""
    return "Vanity URL Customize here... <br> Example for URL : name/Shohag"




@app.route('/name/<title>')
def nameVanityURL(title):
     return "<h2>"+title+"</h2>";




@app.route('/name/<title>')
def vanityURL(title):
    if title=='Shohag':
        return "Hello Shohag, Whats up?";
    else:
        return "<h2>"+title+"</h2>";
    
     