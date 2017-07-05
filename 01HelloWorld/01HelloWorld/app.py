"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/')
def hello():
    """Renders a sample page."""
    return "Hello World Everybody !"


@app.route('/Shohag')
def shohag():
    """Renders a sample page."""
    return "Hello World Shohag "



@app.route('/Html')
def html():
    """Renders a sample page."""
    return """
              <!DOCTYPE html>
                <html>
                    <head>
                       <title>Html Page</title>
                    </head>
                    <body>

                        <h1>My First Html Page</h1>
                        <p>This is a paragraph.</p>

                    </body>
                </html>
          
          """



if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
