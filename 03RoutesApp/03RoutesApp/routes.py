from app import app;



@app.route('/')
def hello():
    """Renders a sample page."""
    return "Hello World!"


@app.route('/Create')
def create(): 
    return "<h1>Create Pages!</h1>"
