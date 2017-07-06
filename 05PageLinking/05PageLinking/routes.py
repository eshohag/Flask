from flask import Flask, url_for;
from app import app;





@app.route('/')
def onePage():   
   #return "<a href='"+url_for('pageTwo')+"'>Go To Next Page</a>";


   #goToNextPage="<a href='"+url_for('pageTwo')+"'>Go To Next Page</a>";
   #return goToNextPage;


   goToNextPage="<a href='"+url_for('pageTwo')+"'>Go To Next Page</a>";
   return """   
             <!DOCTYPE html>
             <html>
                 <head>
                     <title>Page Linking</title>
                 </head>
           
                 <body>
                     <h1 style="color:blue;">"""+goToNextPage+"""</h1>
                 </body>
            </html>   
   """;



@app.route('/secondPage')
def pageTwo():   
    return "Hello second Pages";