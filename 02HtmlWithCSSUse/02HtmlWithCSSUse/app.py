"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/InlineCSS')
def inlineCSS():
    """Renders a sample page."""
    return """
    
            <!DOCTYPE html>
             <html>
                <head>
                    <title>Inline CSS</title>
                </head>
           
                <body>
                  <h1 style="color:blue;">This is a Blue Heading</h1>
                </body>
            </html>
    
    
    
    """



@app.route('/InternalCSS')
def internalCSS():
    """Renders a sample page."""
    return """
    
            <!DOCTYPE html>
            <html>
                <head>
                     <title>Internal CSS</title>
                    <style>
                        body {background-color: powderblue;}
                        h1   {color: blue;}
                        p    {color: red;}
                    </style>
                </head>
                <body>

                    <h1>This is a heading</h1>
                    <p>This is a paragraph.</p>

                </body>
            </html> 
       
    """



@app.route('/ExternalStyleSheet')
def externalStyleSheet():
    """Renders a sample page."""
    return """
    
          <!DOCTYPE html>
        <html>
            <head>
                <title>External Style Sheet</title>
                <link rel="stylesheet" type="text/css" href="styles.css">
                
            </head>
            <body>

                <h1>This is a heading</h1>
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
