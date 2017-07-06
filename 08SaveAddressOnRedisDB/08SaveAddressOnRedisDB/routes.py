from flask import Flask, url_for, request, render_template;
from app import app;
import redis;
#Redis Database Connections code below
r=redis.StrictRedis(host='localhost',port=6379,db=0,charset="utf-8",decode_responses=True);


@app.route('/')
def intro():
    savePage="<a href='"+url_for('save')+"'>Click Here...</a>";
    return """   
             <!DOCTYPE html>
             <html>
                 <head>
                     <title>Save Address</title>
                 </head>
           
                 <body>
                    <div style="text-align:center;">
                        <h1>Welcome to our Address save applications</h1>
                        <h2 style="color:blue;">"""+savePage+"""</h2>
                     </div>
                 </body>
            </html>   
     """;



@app.route('/save', methods=['GET','POST'])
def save():
    if request.method=='GET':
        return render_template('SaveAddressForm.html');

    elif request.method=='POST':
        name=request.form['name'];
        address=request.form['address'];
        try:
            #Redis Database to data store here code...
            r.set(name,address);
            return "Success Save";
        except:
            return "Failed Save";

    else:
        return "Invalid Request";



@app.route('/check/<name>', methods=['GET','POST'])
def check(name):
    if request.method=='GET':
          #return render_template('SaveAddressForm.html');
          #Read Data from Redis database here
          city=r.get(name);          
          return city;
    elif request.method=='POST':
        return "Post Method here..."
    else:
        return "Invalid Request";

    